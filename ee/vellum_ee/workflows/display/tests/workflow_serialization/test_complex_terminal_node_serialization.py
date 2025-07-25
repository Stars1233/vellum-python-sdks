import pytest

from deepdiff import DeepDiff

from vellum_ee.workflows.display.workflows.get_vellum_workflow_display_class import get_workflow_display

from tests.workflows.complex_final_output_node.missing_final_output_node import MissingFinalOutputNodeWorkflow
from tests.workflows.complex_final_output_node.missing_workflow_output import MissingWorkflowOutputWorkflow


def test_serialize_workflow__missing_final_output_node():
    # GIVEN a Workflow that is missing a Terminal Node
    workflow_display = get_workflow_display(workflow_class=MissingFinalOutputNodeWorkflow)

    # WHEN we serialize it
    serialized_workflow: dict = workflow_display.serialize()

    # THEN we should get a serialized representation its output variables to be what we expect
    output_variables = serialized_workflow["output_variables"]
    assert len(output_variables) == 2
    assert not DeepDiff(
        [
            {"id": "a360aef6-3bb4-4c56-b407-478042ef224d", "key": "alpha", "type": "STRING"},
            {"id": "5e6d3ea6-ef91-4937-8fff-f33e07446e6a", "key": "beta", "type": "STRING"},
        ],
        output_variables,
        ignore_order=True,
    )

    # AND each node should be serialized correctly
    workflow_raw_data = serialized_workflow["workflow_raw_data"]
    assert isinstance(workflow_raw_data, dict)

    # AND we should create synthetic terminal nodes for each output variable
    final_output_nodes = [node for node in workflow_raw_data["nodes"] if node["type"] == "TERMINAL"]
    assert not DeepDiff(
        [
            {
                "id": "acc91103-f761-47a5-bdd4-0e5e7650bb30",
                "type": "TERMINAL",
                "data": {
                    "label": "First Final Output Node",
                    "name": "alpha",
                    "target_handle_id": "a0c2eb7a-398e-4f28-b63d-f3bae9b563ee",
                    "output_id": "0cd02933-c5b9-47c9-aede-e97c5870e8aa",
                    "output_type": "STRING",
                    "node_input_id": "16363762-c14a-4162-8fab-525079d3cffe",
                },
                "inputs": [
                    {
                        "id": "16363762-c14a-4162-8fab-525079d3cffe",
                        "key": "node_input",
                        "value": {
                            "rules": [
                                {
                                    "type": "INPUT_VARIABLE",
                                    "data": {"input_variable_id": "da086239-d743-4246-b666-5c91e22fb88c"},
                                }
                            ],
                            "combinator": "OR",
                        },
                    }
                ],
                "display_data": {"position": {"x": 200.0, "y": 75.0}},
                "base": {
                    "name": "FinalOutputNode",
                    "module": ["vellum", "workflows", "nodes", "displayable", "final_output_node", "node"],
                },
                "definition": {
                    "name": "FirstFinalOutputNode",
                    "module": ["tests", "workflows", "complex_final_output_node", "missing_final_output_node"],
                },
                "outputs": [
                    {
                        "id": "0cd02933-c5b9-47c9-aede-e97c5870e8aa",
                        "name": "value",
                        "type": "STRING",
                        "value": {
                            "type": "WORKFLOW_INPUT",
                            "input_variable_id": "da086239-d743-4246-b666-5c91e22fb88c",
                        },
                    }
                ],
            },
            {
                "id": "bb88768d-472e-4997-b7ea-de09163d1b4c",
                "type": "TERMINAL",
                "data": {
                    "label": "Final Output",
                    "name": "beta",
                    "target_handle_id": "5e337b19-cef6-45af-802b-46da4ad7e794",
                    "output_id": "5e6d3ea6-ef91-4937-8fff-f33e07446e6a",
                    "output_type": "STRING",
                    "node_input_id": "590161f1-20ed-4339-9ce3-61aade3a142a",
                },
                "inputs": [
                    {
                        "id": "590161f1-20ed-4339-9ce3-61aade3a142a",
                        "key": "node_input",
                        "value": {
                            "rules": [
                                {
                                    "type": "NODE_OUTPUT",
                                    "data": {
                                        "node_id": "32d88cab-e9fa-4a56-9bc2-fb6e1fd0897f",
                                        "output_id": "04df0e76-690a-4ae1-ab52-fe825a334dcc",
                                    },
                                }
                            ],
                            "combinator": "OR",
                        },
                    }
                ],
                "display_data": {"position": {"x": 400.0, "y": -50.0}},
                "base": {
                    "name": "FinalOutputNode",
                    "module": ["vellum", "workflows", "nodes", "displayable", "final_output_node", "node"],
                },
                "definition": None,
            },
        ],
        final_output_nodes,
        ignore_order=True,
    )


def test_serialize_workflow__missing_workflow_output():
    # GIVEN a Workflow that contains a terminal node that is unreferenced by the Workflow's Outputs
    workflow_display = get_workflow_display(workflow_class=MissingWorkflowOutputWorkflow)

    # WHEN we serialize it, it should throw an error
    with pytest.raises(ValueError) as exc_info:
        workflow_display.serialize()

    assert exc_info.value.args[0] == "Unable to serialize terminal nodes that are not referenced by workflow outputs."
