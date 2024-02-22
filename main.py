# Import Libraries
from google_trans_new import google_translator
import streamlit as st
import PyPDF2
import docx
# import pdftotext

def read_pdf(uploaded_file):
    """
    Extracts and returns all text from a PDF file.

    Parameters:
    - file (str or Path or file object): The path to the PDF file or a file object to be read.
    
    Returns:
    - str: A string containing all the text extracted from the PDF file.

    Raises:
        IOError: If there's an error reading the file.
    """
    try:
        with open(uploaded_file.name, 'wb') as f: 
            f.write(uploaded_file.getvalue())
        with open(uploaded_file.name, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)

            # Get the number of pages in the PDF file
            num_pages = len(pdf_reader.pages)

            # Iterate over each page and print the text content
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text() + "\n"
        return text
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


def read_word(uploaded_file):
    """
    Reads the text content from a Word (.docx) file.

    Args:
        filepath: The path to the Word file.

    Returns:
        str: The extracted text content, or an error message if there's an issue.

    Raises:
        IOError: If there's an error reading the file.
    """

    try:
        with open(uploaded_file.name, 'wb') as f: 
            f.write(uploaded_file.getvalue())

        # Open the file in read mode
        doc = docx.Document(uploaded_file.name)

        # Extract text from paragraphs
        all_text = ""
        for paragraph in doc.paragraphs:
            all_text += paragraph.text + "\n"

        # Return the extracted text
        return all_text

    except IOError as e:
        raise IOError(f"Error reading file: {e}")



st.set_page_config(page_title='Simply! Translate', layout='wide', initial_sidebar_state='expanded')


Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}


translator = google_translator()
st.title("Language Translator:balloon:")


uploaded_file = st.file_uploader("Upload a File", type=["pdf", "docx"])


# Display the content of the uploaded file, if any
if uploaded_file is not None:
    if '.pdf' in uploaded_file.name:
        text = read_pdf(uploaded_file)
    else:
        text = read_word(uploaded_file)

option1 = st.selectbox('Input language', ('english', ))

option2 = st.selectbox('Output language', ('german', 'italian'))

option3 = st.selectbox('Domain', ('generic', 'IT & Technology'))

value1 = Languages[option1]
value2 = Languages[option2]


if st.button('Translate Sentence'):
    if text == "":
        st.warning('Please **enter text** for translation')

    else:
        translate = translator.translate(text, lang_src=value1, lang_tgt=value2)
        st.header("Translation")
        st.info(str(translate))

        # Save the transcript to a text file
        with open("transcript.txt", "w", encoding="utf-8") as f:
            f.write(translate)

        # Provide a download button for the transcript
        st.download_button("Download Transcript", translate)

        st.success("Translation is **successfully** completed!")

else:
    pass

 
 




