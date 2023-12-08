# Import necessary libraries
import os
import streamlit as st
import Gradient
from gradientai import Gradient

os.environ['GRADIENT_ACCESS_TOKEN'] = st.secrets['GRADIENT_ACCESS_TOKEN']
os.environ['GRADIENT_WORKSPACE_ID'] = st.secrets['GRADIENT_WORKSPACE_ID']

def main():
    # Streamlit title and description
    st.title("Interactive Food Drive Assistant")
    st.write("Ask a question about the Food Drive!")

    with Gradient() as gradient:        
        new_model_adapter = gradient.get_model_adapter(model_adapter_id=st.secrets['Model_ID'])

        user_input = st.text_input("Ask your question:")
        if user_input and user_input.lower() not in ['quit', 'exit']:
            sample_query = f"### Instruction: {user_input} \n\n### Response:"
            st.markdown(f"Asking: {sample_query}")

            # before fine-tuning
            completion = new_model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
            st.markdown(f"Generated: {completion}")

        # Delete the model adapter after generating the response
        new_model_adapter.delete()

if __name__ == "__main__":
    main()
