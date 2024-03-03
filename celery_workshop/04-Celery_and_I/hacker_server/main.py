from celery_utils.base_group import BaseGroup


def main():
    # Our MITM operation was successful!
    # we capture packages sent to different users
    # from the atomic bunker at Moscow.
    # We can confirm that the packages
    # contain super important data for the war effort.
    # The packages are encrypted in RSA.

    # We think we can decrypt them by finding the factors of the RSA modulus.
    # here are the modulus we captured:
    modulus_list = [9734017, 13438169, 17169941, 23565991]

    # There is a crypto server you can use to find the factors of the modulus
    # the factorization process can take a while, so we will use a celery worker
    # to do the factorization, and we want to do it in parallel.

    # TODO: add your code here
    # you will need to create a BaseGroup
    # add all the tasks to it
    # run the group and wait for the results
    # TODO: add your code here

    # you can read more about how RSA works here:
    # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation


if __name__ == "__main__":
    main()
