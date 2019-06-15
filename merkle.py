'''
Implementation of a Merkle Tree Hash Algorithm based on this tutorial: https://www.youtube.com/watch?v=GaFuBrkkI_w
'''

import hashlib

class MerkleTreeHash(object):
    def _init_(self):
        pass

        def find_merkle_hash(self, file_hashes):
            # Here we want to find the merkle tree hash of all the file hashes passed to this function. Note we are going to use recursion to solve this problem.

            # This is the single procedure we will follow for finding the hash given a list of hashes we first group all the hashes in twos. Next we concantonate the the hashes in each group and compute the hash of the group, thenkeep track of the group hashes. We will repeat these steps until we have a single hash that becomes the hash we are looking for.

            blocks = []

            if not file_hashes:
                raise ValueError(
                'Missing required file hashes for computing merkle tree hash'
                )

            # First sort the hashes
            for m in sorted(file_hashes):
                blocks.append(m)

                list_len = len(blocks)
                # Adjust the block of hashes until we have an even number of items in the blocks, this entails appeding to the end of the block the last entry. To do this we use the modulus math to determin when we have an even number of items.
                while list_len % 2 != 0:
                    blocks.extend(blocks[-1:])
                    list_len = len(blocks)

                # Now we have an even number of itmes in the block we need to group the itmes in twos.
                secondary = []
                for k in [blocks[x:x+2] for x in xrange(0, len(blocks), 2)]:
                    # Note k is a list with only two itmes, which is what we want. This is so that we can concantonate them and create a new hash from them.
                    hasher = hashlib.sha256()
                    hasher.update(k[0]+k[1])
                    secondary.append(hasher.hexdigest())

                # Now, becuase this is a recursive method, we need to determin hen we only have a single item in the list. This marks the end of the iteration and we can return the last hash as the merkle root.
                if len(secondary) == 1:
                    # Note, we only returning the first 64 characters, however if you want to return the entire hash just remove the last section [0:64].
                    return secondary[0][0:64]
                else:
                    # If the number of items in thelist is more than one, we still need ro iterate through this so we pass it back to the method. We pass the secondary list since it holds the second iteration method results.
                    return self.find_merkle_hash(secondary)

if __name__ == '__main__':

    # Test the class. We will test by generating 13 random hashes and then try to find their merkle tree hash. Note you can always build hashes directly from lists by reading the content of the paths to the hashing then create a list of hashes from it to be passed to this Implementation.
    import uuid
    file_hashes = []

    for i in range(0,13):
        file_hashes.append(str(uuid.uuid4().hex))

        print 'Finding the merkle tree hash of {0} random hashes' .format(
            len(file_hashes)
        )

        cls = MerkleTreeHash()
        mk = cls.find_merkle_hash(file_hashes)
        print 'the merkle tree hash of hashes below is : {0}' .format(mk)
        print '...'
        print file_hashes
        # Now lets go ahead and run the test
