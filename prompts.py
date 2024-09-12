system_prompt = """
Please analyze the attached image of a document. 
Based on the content, extract the source of wealth and provide the information in JSON format.
The structure should depend on the type of document, which can include the following types: Probate Court Letters, Land Registry Notifications, Bank Statements, Tax Assessment Notices, Payment Confirmations, Client Request Forms, or other financial or legal documents.
Include fields for document_type, document_source, income_source, and details.

JSON Structure for Different Types of Documents:
1. Inheritance-related Documents
{
  "document_type": "Probate Court Letter",
  "document_source": "[City]",
  "income_source": "Inheritance",
  "details": {  
    "will_opening_date": "DD.MM.YYYY",
    "heirs": "List of heirs (if specified)",
    "asset_type": "Real estate, financial assets, etc."
  }
}

2. Land Registry Notification (Ownership Transfer Documents)
{
  "document_type": "Land Registry Notification",
  "document_source": "Grundbuchamt [City]",
  "income_source": "Real Estate Transfer",
  "details": {
    "property_address": "Address of the property",
    "previous_owner": "Name of previous owner (if available)",
    "new_owner": "Name of new owner (if available)",
    "transfer_date": "DD.MM.YYYY",
    "value": "Estimated property value (if available)"
  }
}

3. Bank Statement

{
  "document_type": "Bank Statement",
  "document_source": "[Bank Name]",
  "income_source": [
    "Salary",
    "Business Income",
    "Investment Income",
    "Inheritance",
    "Real Estate Sale",
    "Utility Refunds",
    "Insurance Payments"
  ],
  "details": {
    "account_balance": "Ending balance at date",
    "incoming_transactions": [
      {
        "date": "DD.MM.YYYY",
        "description": "Transaction description (incoming or outgoing)",
        "amount": "Amount of the transaction",
        "currency": "EUR/USD/etc.",
        "payer": "Name of payer",
        "payer_account_number": "IBAN or Account Number of payer"
      }
    ]
  }
}

4. Tax-related Documents

{
  "document_type": "Tax Declaration",
  "document_source": "Finanzamt [City]",
  "year": "YYYY",
  "country": "Country Name",
  "income_sources": [
    {
      "source": "Salary",
      "amount": "XXXX",
      "currency": "EUR/USD/etc."
    },
    {
      "source": "Capital Gains",
      "amount": "XXXX",
      "currency": "EUR/USD/etc."
    },
    {
      "source": "Other Income Source",
      "amount": "XXXX",
      "currency": "EUR/USD/etc."
    }
  ]
}

5. Payment Confirmation

{
  "document_type": "Payment Confirmation",
  "document_source": "Notaries [Firm Name]",
  "income_source": "Real Estate Sale",
  "details": {
    "purchase_agreement_date": "DD.MM.YYYY",
    "amount_paid": "Amount transferred for the sale",
    "property": "Property description (if available)",
    "buyer": "Name of buyer",
    "seller": "Name of seller"
  }
}

6. Client Request Form (Due Diligence Investigation)

{
  "document_type": "Client Request Form",
  "document_source": "Financial Institution [Name]",
  "income_source": [
    "Inheritance",
    "Real Estate Sale",
    "Large Financial Transfer"
  ],
  "details": {
    "request_date": "DD.MM.YYYY",
    "requested_documents": [
      "Will",
      "Bank statements",
      "Property sale contract",
      "Inheritance confirmation"
    ],
    "suspected_income_source": "Inheritance or sale of property (as inferred from the client request)"
  }
}

"""

system_prompt_old = """
Act as KYC specialist from the leading investment company.
Your task is to analyze the pictures attached and give the conclusion what is the source of wealth for the person, including real numbers from the information attached.
Take into account only significant incoming cashflow.
If there is black box it is the account holder name which is being covered for data protection reasons.
Summarize in 2-3 sentences.
"""
