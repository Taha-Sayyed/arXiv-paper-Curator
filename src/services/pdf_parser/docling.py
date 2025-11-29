#by taha

import logging
import pypdfium2 as pdfium


from pathlib import Path
from typing import Optional
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from src.exceptions import PDFParsingException, PDFValidationError
from src.schemas.pdf_parser.models import PaperFigure, PaperSection, PaperTable, ParserType, PdfContent


logger = logging.getLogger(__name__)
