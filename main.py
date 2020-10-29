import auth, actions, sys


def setup():
    print("IMPORTANT: "
          "Please make sure to add your public and secret key to the current environment to use this tool. \n"
          "Your Twitter App needs to have Read and Write authorisations enabled.")
    print("------")
    print("Welcome to listefy-CL, a command-line tool to create a list from a specified user followings on Twitter")
    print("N.B: The created list will be private, users won't be notified when added to the list")

    print("After authorising the app, "
          "you will be asked to enter the handle of the user you want to create the list from.\n")
    oauth = auth.authSetup()

    handle = input('Enter the username: ')
    list_name = input('Enter the list name: ')
    actions.createFollowersList(oauth, handle, list_name)

    print("\n\n")
    print("Thank you for using this tool. SPREAD LOVE.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
