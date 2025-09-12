"""Writing flow for report generation."""

from ai_pipeline_core import DocumentList, FlowConfig, pipeline_flow

from ai_summarization.documents.flow import DraftDocument, InputDocument, PlanDocument
from ai_summarization.flow_options import ProjectFlowOptions

from .tasks import write_report


class WritingFlowConfig(FlowConfig):
    """Configuration for writing flow."""

    INPUT_DOCUMENT_TYPES = [InputDocument, PlanDocument]
    OUTPUT_DOCUMENT_TYPE = DraftDocument


@pipeline_flow(config=WritingFlowConfig)
async def writing_flow(
    project_name: str,
    documents: DocumentList,
    flow_options: ProjectFlowOptions,
) -> DocumentList:
    """Write the initial report draft based on the plan."""
    # Get required documents
    input_docs = documents.filter_by(InputDocument)
    plan_doc = documents.get_by(PlanDocument)

    # Write the draft
    draft_doc = await write_report(
        input_documents=input_docs,
        plan_document=plan_doc,
        model=flow_options.core_model,
        task_description=flow_options.task_description,
    )

    # Return validated output
    return WritingFlowConfig.create_and_validate_output([draft_doc])
