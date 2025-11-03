"""Planning flow for report generation."""

from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow

from ai_summarization.documents.flow import InputDocument, PlanDocument
from ai_summarization.flow_options import ProjectFlowOptions

from .tasks import plan_report


class PlanningFlowConfig(FlowConfig):
    """Configuration for planning flow."""

    INPUT_DOCUMENT_TYPES = [InputDocument]
    OUTPUT_DOCUMENT_TYPE = PlanDocument


@pipeline_flow(config=PlanningFlowConfig)
async def planning_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Plan the report structure based on input documents."""
    # Get input documents
    input_docs = documents.filter_by(InputDocument)

    # Create the plan
    plan_doc = await plan_report(
        input_documents=input_docs,
        model=flow_options.core_model,
    )

    # Return validated output
    return PlanningFlowConfig.create_and_validate_output(plan_doc)
