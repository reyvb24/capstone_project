from send_email import create_template, extract_contacts, extract_summary, authenticate_account, create_plot
import fire

if __name__ == '__main__':
  # Export to Fire
  fire.Fire(create_plot)