import daes

test_key = "f4eba54dab7b4cdcb34f13689beea128acdc8960c8ec4c929d0c9f85d2fa5c22" # 256-bit (64 character) hex key
int_test_key = daes.hexToKey(test_key)
plain="hello world"
cipher = daes.encrypt(plain, int_test_key)
print("\ncipher text -",cipher)