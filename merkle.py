###
Implementation of a Merkle Tree Hash Algorithm in Python based on this tutorial: https://www.youtube.com/watch?v=GaFuBrkkI_w
###

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

                    
