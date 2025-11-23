def parse_input(user_input: str):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args


def help_text() -> str:
    return (
        "Available commands:\n"
        "  hello                             -> greeting\n"
        "  add <name> <phone>                -> add contact or append phone\n"
        "  change <name> <new_phone>         -> replace single phone with new\n"
        "  change <name> <old> <new>         -> replace specific old phone\n"
        "  phone <name>                      -> show phones for contact\n"
        "  addphone <name> <phone>           -> add phone to existing contact\n"
        "  removephone <name> <phone>        -> remove specific phone\n"
        "  find <name>                       -> show full contact line\n"
        "  add-birthday <name> <DD.MM.YYYY>  -> add birthday to contact\n"
        "  show-birthday <name>              -> show birthday of contact\n"
        "  birthdays                         -> upcoming birthdays for 7 days\n"
        "  delete <name>                     -> delete contact\n"
        "  all                               -> show all contacts\n"
        "  help                              -> show this help\n"
        "  exit | close                      -> quit\n"
    )
