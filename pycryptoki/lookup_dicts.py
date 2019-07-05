"""
Module that contains lookup dictionaries for easy logging of
error codes and other constants within pycryptoki.
"""

from .defines import *

#:
ret_vals_dictionary = {
    CKR_OK: 'CKR_OK',
    CKR_CANCEL: 'CKR_CANCEL',
    CKR_HOST_MEMORY: 'CKR_HOST_MEMORY',
    CKR_SLOT_ID_INVALID: 'CKR_SLOT_ID_INVALID',
    CKR_GENERAL_ERROR: 'CKR_GENERAL_ERROR',
    CKR_FUNCTION_FAILED: 'CKR_FUNCTION_FAILED',
    CKR_ARGUMENTS_BAD: 'CKR_ARGUMENTS_BAD',
    CKR_NO_EVENT: 'CKR_NO_EVENT',
    CKR_NEED_TO_CREATE_THREADS: 'CKR_NEED_TO_CREATE_THREADS',
    CKR_CANT_LOCK: 'CKR_CANT_LOCK',
    CKR_ATTRIBUTE_READ_ONLY: 'CKR_ATTRIBUTE_READ_ONLY',
    CKR_ATTRIBUTE_SENSITIVE: 'CKR_ATTRIBUTE_SENSITIVE',
    CKR_ATTRIBUTE_TYPE_INVALID: 'CKR_ATTRIBUTE_TYPE_INVALID',
    CKR_ATTRIBUTE_VALUE_INVALID: 'CKR_ATTRIBUTE_VALUE_INVALID',
    CKR_DATA_INVALID: 'CKR_DATA_INVALID',
    CKR_DATA_LEN_RANGE: 'CKR_DATA_LEN_RANGE',
    CKR_DEVICE_ERROR: 'CKR_DEVICE_ERROR',
    CKR_DEVICE_MEMORY: 'CKR_DEVICE_MEMORY',
    CKR_DEVICE_REMOVED: 'CKR_DEVICE_REMOVED',
    CKR_ENCRYPTED_DATA_INVALID: 'CKR_ENCRYPTED_DATA_INVALID',
    CKR_ENCRYPTED_DATA_LEN_RANGE: 'CKR_ENCRYPTED_DATA_LEN_RANGE',
    CKR_FUNCTION_CANCELED: 'CKR_FUNCTION_CANCELED',
    CKR_FUNCTION_NOT_PARALLEL: 'CKR_FUNCTION_NOT_PARALLEL',
    CKR_FUNCTION_NOT_SUPPORTED: 'CKR_FUNCTION_NOT_SUPPORTED',
    CKR_KEY_HANDLE_INVALID: 'CKR_KEY_HANDLE_INVALID',
    CKR_KEY_SIZE_RANGE: 'CKR_KEY_SIZE_RANGE',
    CKR_KEY_TYPE_INCONSISTENT: 'CKR_KEY_TYPE_INCONSISTENT',
    CKR_KEY_NOT_NEEDED: 'CKR_KEY_NOT_NEEDED',
    CKR_KEY_CHANGED: 'CKR_KEY_CHANGED',
    CKR_KEY_NEEDED: 'CKR_KEY_NEEDED',
    CKR_KEY_INDIGESTIBLE: 'CKR_KEY_INDIGESTIBLE',
    CKR_KEY_FUNCTION_NOT_PERMITTED: 'CKR_KEY_FUNCTION_NOT_PERMITTED',
    CKR_KEY_NOT_WRAPPABLE: 'CKR_KEY_NOT_WRAPPABLE',
    CKR_KEY_UNEXTRACTABLE: 'CKR_KEY_UNEXTRACTABLE',
    CKR_MECHANISM_INVALID: 'CKR_MECHANISM_INVALID',
    CKR_MECHANISM_PARAM_INVALID: 'CKR_MECHANISM_PARAM_INVALID',
    CKR_OBJECT_HANDLE_INVALID: 'CKR_OBJECT_HANDLE_INVALID',
    CKR_OPERATION_ACTIVE: 'CKR_OPERATION_ACTIVE',
    CKR_OPERATION_NOT_INITIALIZED: 'CKR_OPERATION_NOT_INITIALIZED',
    CKR_PIN_INCORRECT: 'CKR_PIN_INCORRECT',
    CKR_PIN_INVALID: 'CKR_PIN_INVALID',
    CKR_PIN_LEN_RANGE: 'CKR_PIN_LEN_RANGE',
    CKR_PIN_EXPIRED: 'CKR_PIN_EXPIRED',
    CKR_PIN_LOCKED: 'CKR_PIN_LOCKED',
    CKR_SESSION_CLOSED: 'CKR_SESSION_CLOSED',
    CKR_SESSION_COUNT: 'CKR_SESSION_COUNT',
    CKR_SESSION_HANDLE_INVALID: 'CKR_SESSION_HANDLE_INVALID',
    CKR_SESSION_PARALLEL_NOT_SUPPORTED: 'CKR_SESSION_PARALLEL_NOT_SUPPORTED',
    CKR_SESSION_READ_ONLY: 'CKR_SESSION_READ_ONLY',
    CKR_SESSION_EXISTS: 'CKR_SESSION_EXISTS',
    CKR_SESSION_READ_ONLY_EXISTS: 'CKR_SESSION_READ_ONLY_EXISTS',
    CKR_SESSION_READ_WRITE_SO_EXISTS: 'CKR_SESSION_READ_WRITE_SO_EXISTS',
    CKR_SIGNATURE_INVALID: 'CKR_SIGNATURE_INVALID',
    CKR_SIGNATURE_LEN_RANGE: 'CKR_SIGNATURE_LEN_RANGE',
    CKR_TEMPLATE_INCOMPLETE: 'CKR_TEMPLATE_INCOMPLETE',
    CKR_TEMPLATE_INCONSISTENT: 'CKR_TEMPLATE_INCONSISTENT',
    CKR_TOKEN_NOT_PRESENT: 'CKR_TOKEN_NOT_PRESENT',
    CKR_TOKEN_NOT_RECOGNIZED: 'CKR_TOKEN_NOT_RECOGNIZED',
    CKR_TOKEN_WRITE_PROTECTED: 'CKR_TOKEN_WRITE_PROTECTED',
    CKR_UNWRAPPING_KEY_HANDLE_INVALID: 'CKR_UNWRAPPING_KEY_HANDLE_INVALID',
    CKR_UNWRAPPING_KEY_SIZE_RANGE: 'CKR_UNWRAPPING_KEY_SIZE_RANGE',
    CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT: 'CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT',
    CKR_USER_ALREADY_LOGGED_IN: 'CKR_USER_ALREADY_LOGGED_IN',
    CKR_USER_NOT_LOGGED_IN: 'CKR_USER_NOT_LOGGED_IN',
    CKR_USER_PIN_NOT_INITIALIZED: 'CKR_USER_PIN_NOT_INITIALIZED',
    CKR_USER_TYPE_INVALID: 'CKR_USER_TYPE_INVALID',
    CKR_USER_ANOTHER_ALREADY_LOGGED_IN: 'CKR_USER_ANOTHER_ALREADY_LOGGED_IN',
    CKR_USER_TOO_MANY_TYPES: 'CKR_USER_TOO_MANY_TYPES',
    CKR_WRAPPED_KEY_INVALID: 'CKR_WRAPPED_KEY_INVALID',
    CKR_WRAPPED_KEY_LEN_RANGE: 'CKR_WRAPPED_KEY_LEN_RANGE',
    CKR_WRAPPING_KEY_HANDLE_INVALID: 'CKR_WRAPPING_KEY_HANDLE_INVALID',
    CKR_WRAPPING_KEY_SIZE_RANGE: 'CKR_WRAPPING_KEY_SIZE_RANGE',
    CKR_WRAPPING_KEY_TYPE_INCONSISTENT: 'CKR_WRAPPING_KEY_TYPE_INCONSISTENT',
    CKR_RANDOM_SEED_NOT_SUPPORTED: 'CKR_RANDOM_SEED_NOT_SUPPORTED',
    CKR_RANDOM_NO_RNG: 'CKR_RANDOM_NO_RNG',
    CKR_DOMAIN_PARAMS_INVALID: 'CKR_DOMAIN_PARAMS_INVALID',
    CKR_BUFFER_TOO_SMALL: 'CKR_BUFFER_TOO_SMALL',
    CKR_SAVED_STATE_INVALID: 'CKR_SAVED_STATE_INVALID',
    CKR_INFORMATION_SENSITIVE: 'CKR_INFORMATION_SENSITIVE',
    CKR_STATE_UNSAVEABLE: 'CKR_STATE_UNSAVEABLE',
    CKR_CRYPTOKI_NOT_INITIALIZED: 'CKR_CRYPTOKI_NOT_INITIALIZED',
    CKR_CRYPTOKI_ALREADY_INITIALIZED: 'CKR_CRYPTOKI_ALREADY_INITIALIZED',
    CKR_MUTEX_BAD: 'CKR_MUTEX_BAD',
    CKR_MUTEX_NOT_LOCKED: 'CKR_MUTEX_NOT_LOCKED',
    CKR_NEW_PIN_MODE: 'CKR_NEW_PIN_MODE',
    CKR_NEXT_OTP: 'CKR_NEXT_OTP',
    CKR_FUNCTION_REJECTED: 'CKR_FUNCTION_REJECTED',
    CKR_VENDOR_DEFINED: 'CKR_VENDOR_DEFINED',
    CKR_INSERTION_CALLBACK_NOT_SUPPORTED: 'CKR_INSERTION_CALLBACK_NOT_SUPPORTED',
    CKR_FUNCTION_PARALLEL: 'CKR_FUNCTION_PARALLEL',
    CKR_SESSION_EXCLUSIVE_EXISTS: 'CKR_SESSION_EXCLUSIVE_EXISTS',
    CKR_RC_ERROR: 'CKR_RC_ERROR',
    CKR_CONTAINER_HANDLE_INVALID: 'CKR_CONTAINER_HANDLE_INVALID',
    CKR_TOO_MANY_CONTAINERS: 'CKR_TOO_MANY_CONTAINERS',
    CKR_USER_LOCKED_OUT: 'CKR_USER_LOCKED_OUT',
    CKR_CLONING_PARAMETER_ALREADY_EXISTS: 'CKR_CLONING_PARAMETER_ALREADY_EXISTS',
    CKR_CLONING_PARAMETER_MISSING: 'CKR_CLONING_PARAMETER_MISSING',
    CKR_CERTIFICATE_DATA_MISSING: 'CKR_CERTIFICATE_DATA_MISSING',
    CKR_CERTIFICATE_DATA_INVALID: 'CKR_CERTIFICATE_DATA_INVALID',
    CKR_ACCEL_DEVICE_ERROR: 'CKR_ACCEL_DEVICE_ERROR',
    CKR_WRAPPING_ERROR: 'CKR_WRAPPING_ERROR',
    CKR_UNWRAPPING_ERROR: 'CKR_UNWRAPPING_ERROR',
    CKR_MAC_MISSING: 'CKR_MAC_MISSING',
    CKR_DAC_POLICY_PID_MISMATCH: 'CKR_DAC_POLICY_PID_MISMATCH',
    CKR_DAC_MISSING: 'CKR_DAC_MISSING',
    CKR_BAD_DAC: 'CKR_BAD_DAC',
    CKR_SSK_MISSING: 'CKR_SSK_MISSING',
    CKR_BAD_MAC: 'CKR_BAD_MAC',
    CKR_DAK_MISSING: 'CKR_DAK_MISSING',
    CKR_BAD_DAK: 'CKR_BAD_DAK',
    CKR_SIM_AUTHORIZATION_FAILED: 'CKR_SIM_AUTHORIZATION_FAILED',
    CKR_SIM_VERSION_UNSUPPORTED: 'CKR_SIM_VERSION_UNSUPPORTED',
    CKR_SIM_CORRUPT_DATA: 'CKR_SIM_CORRUPT_DATA',
    CKR_USER_NOT_AUTHORIZED: 'CKR_USER_NOT_AUTHORIZED',
    CKR_MAX_OBJECT_COUNT_EXCEEDED: 'CKR_MAX_OBJECT_COUNT_EXCEEDED',
    CKR_SO_LOGIN_FAILURE_THRESHOLD: 'CKR_SO_LOGIN_FAILURE_THRESHOLD',
    CKR_SIM_AUTHFORM_INVALID: 'CKR_SIM_AUTHFORM_INVALID',
    CKR_CITS_DAK_MISSING: 'CKR_CITS_DAK_MISSING',
    CKR_UNABLE_TO_CONNECT: 'CKR_UNABLE_TO_CONNECT',
    CKR_PARTITION_DISABLED: 'CKR_PARTITION_DISABLED',
    CKR_CALLBACK_ERROR: 'CKR_CALLBACK_ERROR',
    CKR_SECURITY_PARAMETER_MISSING: 'CKR_SECURITY_PARAMETER_MISSING',
    CKR_SP_TIMEOUT: 'CKR_SP_TIMEOUT',
    CKR_TIMEOUT: 'CKR_TIMEOUT',
    CKR_ECC_UNKNOWN_CURVE: 'CKR_ECC_UNKNOWN_CURVE',
    CKR_MTK_ZEROIZED: 'CKR_MTK_ZEROIZED',
    CKR_MTK_STATE_INVALID: 'CKR_MTK_STATE_INVALID',
    CKR_INVALID_ENTRY_TYPE: 'CKR_INVALID_ENTRY_TYPE',
    CKR_MTK_SPLIT_INVALID: 'CKR_MTK_SPLIT_INVALID',
    CKR_HSM_STORAGE_FULL: 'CKR_HSM_STORAGE_FULL',
    CKR_DEVICE_TIMEOUT: 'CKR_DEVICE_TIMEOUT',
    CKR_CONTAINER_OBJECT_STORAGE_FULL: 'CKR_CONTAINER_OBJECT_STORAGE_FULL',
    CKR_PED_CLIENT_NOT_RUNNING: 'CKR_PED_CLIENT_NOT_RUNNING',
    CKR_PED_UNPLUGGED: 'CKR_PED_UNPLUGGED',
    CKR_ECC_POINT_INVALID: 'CKR_ECC_POINT_INVALID',
    CKR_OPERATION_NOT_ALLOWED: 'CKR_OPERATION_NOT_ALLOWED',
    CKR_LICENSE_CAPACITY_EXCEEDED: 'CKR_LICENSE_CAPACITY_EXCEEDED',
    CKR_LOG_FILE_NOT_OPEN: 'CKR_LOG_FILE_NOT_OPEN',
    CKR_LOG_FILE_WRITE_ERROR: 'CKR_LOG_FILE_WRITE_ERROR',
    CKR_LOG_BAD_FILE_NAME: 'CKR_LOG_BAD_FILE_NAME',
    CKR_LOG_FULL: 'CKR_LOG_FULL',
    CKR_LOG_NO_KCV: 'CKR_LOG_NO_KCV',
    CKR_LOG_BAD_RECORD_HMAC: 'CKR_LOG_BAD_RECORD_HMAC',
    CKR_LOG_BAD_TIME: 'CKR_LOG_BAD_TIME',
    CKR_LOG_AUDIT_NOT_INITIALIZED: 'CKR_LOG_AUDIT_NOT_INITIALIZED',
    CKR_LOG_RESYNC_NEEDED: 'CKR_LOG_RESYNC_NEEDED',
    CKR_AUDIT_LOGIN_TIMEOUT_IN_PROGRESS: 'CKR_AUDIT_LOGIN_TIMEOUT_IN_PROGRESS',
    CKR_AUDIT_LOGIN_FAILURE_THRESHOLD: 'CKR_AUDIT_LOGIN_FAILURE_THRESHOLD',
    CKR_INVALID_FUF_TARGET: 'CKR_INVALID_FUF_TARGET',
    CKR_INVALID_FUF_HEADER: 'CKR_INVALID_FUF_HEADER',
    CKR_INVALID_FUF_VERSION: 'CKR_INVALID_FUF_VERSION',
    CKR_ECC_ECC_RESULT_AT_INF: 'CKR_ECC_ECC_RESULT_AT_INF',
    CKR_AGAIN: 'CKR_AGAIN',
    CKR_TOKEN_COPIED: 'CKR_TOKEN_COPIED',
    CKR_SLOT_NOT_EMPTY: 'CKR_SLOT_NOT_EMPTY',
    CKR_USER_ALREADY_ACTIVATED: 'CKR_USER_ALREADY_ACTIVATED',
    CKR_STC_NO_CONTEXT: 'CKR_STC_NO_CONTEXT',
    CKR_STC_CLIENT_IDENTITY_NOT_CONFIGURED: 'CKR_STC_CLIENT_IDENTITY_NOT_CONFIGURED',
    CKR_STC_PARTITION_IDENTITY_NOT_CONFIGURED: 'CKR_STC_PARTITION_IDENTITY_NOT_CONFIGURED',
    CKR_STC_DH_KEYGEN_ERROR: 'CKR_STC_DH_KEYGEN_ERROR',
    CKR_STC_CIPHER_SUITE_REJECTED: 'CKR_STC_CIPHER_SUITE_REJECTED',
    CKR_STC_DH_KEY_NOT_FROM_SAME_GROUP: 'CKR_STC_DH_KEY_NOT_FROM_SAME_GROUP',
    CKR_STC_COMPUTE_DH_KEY_ERROR: 'CKR_STC_COMPUTE_DH_KEY_ERROR',
    CKR_STC_FIRST_PHASE_KDF_ERROR: 'CKR_STC_FIRST_PHASE_KDF_ERROR',
    CKR_STC_SECOND_PHASE_KDF_ERROR: 'CKR_STC_SECOND_PHASE_KDF_ERROR',
    CKR_STC_KEY_CONFIRMATION_FAILED: 'CKR_STC_KEY_CONFIRMATION_FAILED',
    CKR_STC_NO_SESSION_KEY: 'CKR_STC_NO_SESSION_KEY',
    CKR_STC_RESPONSE_BAD_MAC: 'CKR_STC_RESPONSE_BAD_MAC',
    CKR_STC_NOT_ENABLED: 'CKR_STC_NOT_ENABLED',
    CKR_STC_CLIENT_HANDLE_INVALID: 'CKR_STC_CLIENT_HANDLE_INVALID',
    CKR_STC_SESSION_INVALID: 'CKR_STC_SESSION_INVALID',
    CKR_STC_CONTAINER_INVALID: 'CKR_STC_CONTAINER_INVALID',
    CKR_STC_SEQUENCE_NUM_INVALID: 'CKR_STC_SEQUENCE_NUM_INVALID',
    CKR_STC_NO_CHANNEL: 'CKR_STC_NO_CHANNEL',
    CKR_STC_RESPONSE_DECRYPT_ERROR: 'CKR_STC_RESPONSE_DECRYPT_ERROR',
    CKR_STC_RESPONSE_REPLAYED: 'CKR_STC_RESPONSE_REPLAYED',
    CKR_STC_REKEY_CHANNEL_MISMATCH: 'CKR_STC_REKEY_CHANNEL_MISMATCH',
    CKR_STC_RSA_ENCRYPT_ERROR: 'CKR_STC_RSA_ENCRYPT_ERROR',
    CKR_STC_RSA_SIGN_ERROR: 'CKR_STC_RSA_SIGN_ERROR',
    CKR_STC_RSA_DECRYPT_ERROR: 'CKR_STC_RSA_DECRYPT_ERROR',
    CKR_STC_RESPONSE_UNEXPECTED_KEY: 'CKR_STC_RESPONSE_UNEXPECTED_KEY',
    CKR_STC_UNEXPECTED_NONCE_PAYLOAD_SIZE: 'CKR_STC_UNEXPECTED_NONCE_PAYLOAD_SIZE',
    CKR_STC_UNEXPECTED_DH_DATA_SIZE: 'CKR_STC_UNEXPECTED_DH_DATA_SIZE',
    CKR_STC_OPEN_CIPHER_MISMATCH: 'CKR_STC_OPEN_CIPHER_MISMATCH',
    CKR_STC_OPEN_DHNIST_PUBKEY_ERROR: 'CKR_STC_OPEN_DHNIST_PUBKEY_ERROR',
    CKR_STC_OPEN_KEY_MATERIAL_GEN_FAIL: 'CKR_STC_OPEN_KEY_MATERIAL_GEN_FAIL',
    CKR_STC_OPEN_RESP_GEN_FAIL: 'CKR_STC_OPEN_RESP_GEN_FAIL',
    CKR_STC_ACTIVATE_MACTAG_U_VERIFY_FAIL: 'CKR_STC_ACTIVATE_MACTAG_U_VERIFY_FAIL',
    CKR_STC_ACTIVATE_MACTAG_V_GEN_FAIL: 'CKR_STC_ACTIVATE_MACTAG_V_GEN_FAIL',
    CKR_STC_ACTIVATE_RESP_GEN_FAIL: 'CKR_STC_ACTIVATE_RESP_GEN_FAIL',
    CKR_CHALLENGE_INCORRECT: 'CKR_CHALLENGE_INCORRECT',
    CKR_ACCESS_ID_INVALID: 'CKR_ACCESS_ID_INVALID',
    CKR_ACCESS_ID_ALREADY_EXISTS: 'CKR_ACCESS_ID_ALREADY_EXISTS',
    CKR_OBJECT_READ_ONLY: 'CKR_OBJECT_READ_ONLY',
    CKR_OBJECT_ALREADY_EXISTS: 'CKR_OBJECT_ALREADY_EXISTS',
    CKR_KEY_NOT_ACTIVE: 'CKR_KEY_NOT_ACTIVE',
    CKR_KEK_RETRY_FAILURE: 'CKR_KEK_RETRY_FAILURE',
    CKR_RNG_RESEED_TOO_EARLY: 'CKR_RNG_RESEED_TOO_EARLY',
    CKR_AUTH_DATA_INCORRECT: 'CKR_AUTH_DATA_INCORRECT',
    CKR_KEY_NOT_AUTHORIZED: 'CKR_KEY_NOT_AUTHORIZED',
    CKR_KEY_CANNOT_BE_AUTHORIZED: 'CKR_KEY_CANNOT_BE_AUTHORIZED',
    CKR_OH_AUTH_DATA_NOT_PROVIDED: 'CKR_OH_AUTH_DATA_NOT_PROVIDED',
    CKR_INVALID_UTILIZATION_METRICS: 'CKR_INVALID_UTILIZATION_METRICS',
    CKR_ASSIGNED_KEY_REQUIRES_AUTH_DATA: 'CKR_ASSIGNED_KEY_REQUIRES_AUTH_DATA',
    CKR_ROLE_CANNOT_MAKE_KEYS_ASSIGNED: 'CKR_ROLE_CANNOT_MAKE_KEYS_ASSIGNED',
    CKR_INVALID_ASSIGNED_ATTRIBUTE_TRANSITION: 'CKR_INVALID_ASSIGNED_ATTRIBUTE_TRANSITION',
    CKR_AUTH_DATA_TOO_LARGE: 'CKR_AUTH_DATA_TOO_LARGE',
    CKR_AUTH_DATA_TOO_SMALL: 'CKR_AUTH_DATA_TOO_SMALL',
    CKR_ASSIGNED_KEY_FAILED_ATTRIBUTE_DEPENDENCIES:
        'CKR_ASSIGNED_KEY_FAILED_ATTRIBUTE_DEPENDENCIES',
}

#:
ATTR_NAME_LOOKUP = {
    CKA_CLASS: 'CKA_CLASS',
    CKA_CERTIFICATE_TYPE: 'CKA_CERTIFICATE_TYPE',
    CKA_KEY_TYPE: 'CKA_KEY_TYPE',
    CKA_VALUE_LEN: 'CKA_VALUE_LEN',
    CKA_MODULUS_BITS: 'CKA_MODULUS_BITS',
    CKA_PRIME_BITS: 'CKA_PRIME_BITS',
    CKA_SUBPRIME_BITS: 'CKA_SUBPRIME_BITS',
    CKA_VALUE_BITS: 'CKA_VALUE_BITS',
    CKA_TOKEN: 'CKA_TOKEN',
    CKA_PRIVATE: 'CKA_PRIVATE',
    CKA_SENSITIVE: 'CKA_SENSITIVE',
    CKA_ENCRYPT: 'CKA_ENCRYPT',
    CKA_DECRYPT: 'CKA_DECRYPT',
    CKA_WRAP: 'CKA_WRAP',
    CKA_UNWRAP: 'CKA_UNWRAP',
    CKA_SIGN: 'CKA_SIGN',
    CKA_SIGN_RECOVER: 'CKA_SIGN_RECOVER',
    CKA_VERIFY: 'CKA_VERIFY',
    CKA_VERIFY_RECOVER: 'CKA_VERIFY_RECOVER',
    CKA_DERIVE: 'CKA_DERIVE',
    CKA_CCM_PRIVATE: 'CKA_CCM_PRIVATE',
    CKA_LOCAL: 'CKA_LOCAL',
    CKA_MODIFIABLE: 'CKA_MODIFIABLE',
    CKA_EXTRACTABLE: 'CKA_EXTRACTABLE',
    CKA_ALWAYS_SENSITIVE: 'CKA_ALWAYS_SENSITIVE',
    CKA_NEVER_EXTRACTABLE: 'CKA_NEVER_EXTRACTABLE',
    CKA_X9_31_GENERATED: 'CKA_X9_31_GENERATED',
    CKA_LABEL: 'CKA_LABEL',
    CKA_APPLICATION: 'CKA_APPLICATION',
    CKA_ISSUER: 'CKA_ISSUER',
    CKA_SUBJECT: 'CKA_SUBJECT',
    CKA_ID: 'CKA_ID',
    CKA_EKM_UID: 'CKA_EKM_UID',
    CKA_GENERIC_1: 'CKA_GENERIC_1',
    CKA_GENERIC_2: 'CKA_GENERIC_2',
    CKA_GENERIC_3: 'CKA_GENERIC_3',
    CKA_START_DATE: 'CKA_START_DATE',
    CKA_END_DATE: 'CKA_END_DATE',
    CKA_VALUE: 'CKA_VALUE',
    CKA_SERIAL_NUMBER: 'CKA_SERIAL_NUMBER',
    CKA_MODULUS: 'CKA_MODULUS',
    CKA_PUBLIC_EXPONENT: 'CKA_PUBLIC_EXPONENT',
    CKA_PRIVATE_EXPONENT: 'CKA_PRIVATE_EXPONENT',
    CKA_PRIME_1: 'CKA_PRIME_1',
    CKA_PRIME_2: 'CKA_PRIME_2',
    CKA_EXPONENT_1: 'CKA_EXPONENT_1',
    CKA_EXPONENT_2: 'CKA_EXPONENT_2',
    CKA_COEFFICIENT: 'CKA_COEFFICIENT',
    CKA_PRIME: 'CKA_PRIME',
    CKA_SUBPRIME: 'CKA_SUBPRIME',
    CKA_BASE: 'CKA_BASE',
    CKA_FINGERPRINT_SHA1: 'CKA_FINGERPRINT_SHA1',
    CKA_FINGERPRINT_SHA256: 'CKA_FINGERPRINT_SHA256',
    CKA_USAGE_COUNT: 'CKA_USAGE_COUNT',
    CKA_USAGE_LIMIT: 'CKA_USAGE_LIMIT',
    CKA_BYTES_REMAINING: 'CKA_BYTES_REMAINING',
    CKA_OUID: 'CKA_OUID',
    CKA_UNWRAP_TEMPLATE: 'CKA_UNWRAP_TEMPLATE',
    CKA_DERIVE_TEMPLATE: 'CKA_DERIVE_TEMPLATE',
    CKA_EC_PARAMS: 'CKA_EC_PARAMS',
    CKA_EC_POINT: 'CKA_EC_POINT',
    CKA_AUTH_DATA: 'CKA_AUTH_DATA',
    CKA_ASSIGNED: 'CKA_ASSIGNED',
    CKA_KEY_STATUS: 'CKA_KEY_STATUS',
    CKA_FAILED_KEY_AUTH_COUNT: 'CKA_FAILED_KEY_AUTH_COUNT'
}

MECH_NAME_LOOKUP = {
    0x00000000: "CKM_RSA_PKCS_KEY_PAIR_GEN",
    0x00000001: "CKM_RSA_PKCS",
    0x00000002: "CKM_RSA_9796",
    0x00000003: "CKM_RSA_X_509",
    0x00000004: "CKM_MD2_RSA_PKCS",
    0x00000005: "CKM_MD5_RSA_PKCS",
    0x00000006: "CKM_SHA1_RSA_PKCS",
    0x00000007: "CKM_RIPEMD128_RSA_PKCS",
    0x00000008: "CKM_RIPEMD160_RSA_PKCS",
    0x00000009: "CKM_RSA_PKCS_OAEP",
    0x0000000A: "CKM_RSA_X9_31_KEY_PAIR_GEN",
    0x0000000B: "CKM_RSA_X9_31",
    0x0000000C: "CKM_SHA1_RSA_X9_31",
    0x0000000D: "CKM_RSA_PKCS_PSS",
    0x0000000E: "CKM_SHA1_RSA_PKCS_PSS",
    0x00000010: "CKM_DSA_KEY_PAIR_GEN",
    0x00000011: "CKM_DSA",
    0x00000012: "CKM_DSA_SHA1",
    0x00000020: "CKM_DH_PKCS_KEY_PAIR_GEN",
    0x00000021: "CKM_DH_PKCS_DERIVE",
    0x00000030: "CKM_X9_42_DH_KEY_PAIR_GEN",
    0x00000031: "CKM_X9_42_DH_DERIVE",
    0x00000032: "CKM_X9_42_DH_HYBRID_DERIVE",
    0x00000033: "CKM_X9_42_MQV_DERIVE",
    0x00000040: "CKM_SHA256_RSA_PKCS",
    0x00000041: "CKM_SHA384_RSA_PKCS",
    0x00000042: "CKM_SHA512_RSA_PKCS",
    0x00000043: "CKM_SHA256_RSA_PKCS_PSS",
    0x00000044: "CKM_SHA384_RSA_PKCS_PSS",
    0x00000045: "CKM_SHA512_RSA_PKCS_PSS",
    0x00000046: "CKM_SHA224_RSA_PKCS",
    0x00000047: "CKM_SHA224_RSA_PKCS_PSS",
    0x00000100: "CKM_RC2_KEY_GEN",
    0x00000101: "CKM_RC2_ECB",
    0x00000102: "CKM_RC2_CBC",
    0x00000103: "CKM_RC2_MAC",
    0x00000104: "CKM_RC2_MAC_GENERAL",
    0x00000105: "CKM_RC2_CBC_PAD",
    0x00000110: "CKM_RC4_KEY_GEN",
    0x00000111: "CKM_RC4",
    0x00000120: "CKM_DES_KEY_GEN",
    0x00000121: "CKM_DES_ECB",
    0x00000122: "CKM_DES_CBC",
    0x00000123: "CKM_DES_MAC",
    0x00000124: "CKM_DES_MAC_GENERAL",
    0x00000125: "CKM_DES_CBC_PAD",
    0x00000130: "CKM_DES2_KEY_GEN",
    0x00000131: "CKM_DES3_KEY_GEN",
    0x00000132: "CKM_DES3_ECB",
    0x00001102: "CKM_DES3_ECB_ENCRYPT_DATA",
    0x00000133: "CKM_DES3_CBC",
    0x00001103: "CKM_DES3_CBC_ENCRYPT_DATA",
    0x00000134: "CKM_DES3_MAC",
    0x00000135: "CKM_DES3_MAC_GENERAL",
    0x00000136: "CKM_DES3_CBC_PAD",
    0x00000137: "CKM_DES3_CMAC_GENERAL",
    0x00000138: "CKM_DES3_CMAC",
    0x00000140: "CKM_CDMF_KEY_GEN",
    0x00000141: "CKM_CDMF_ECB",
    0x00000142: "CKM_CDMF_CBC",
    0x00000143: "CKM_CDMF_MAC",
    0x00000144: "CKM_CDMF_MAC_GENERAL",
    0x00000145: "CKM_CDMF_CBC_PAD",
    0x00000150: "CKM_DES_OFB64",
    0x00000151: "CKM_DES_OFB8",
    0x00000152: "CKM_DES_CFB64",
    0x00000153: "CKM_DES_CFB8",
    0x00000200: "CKM_MD2",
    0x00000201: "CKM_MD2_HMAC",
    0x00000202: "CKM_MD2_HMAC_GENERAL",
    0x00000210: "CKM_MD5",
    0x00000211: "CKM_MD5_HMAC",
    0x00000212: "CKM_MD5_HMAC_GENERAL",
    0x00000220: "CKM_SHA_1",
    0x00000221: "CKM_SHA_1_HMAC",
    0x00000222: "CKM_SHA_1_HMAC_GENERAL",
    0x00000230: "CKM_RIPEMD128",
    0x00000231: "CKM_RIPEMD128_HMAC",
    0x00000232: "CKM_RIPEMD128_HMAC_GENERAL",
    0x00000240: "CKM_RIPEMD160",
    0x00000241: "CKM_RIPEMD160_HMAC",
    0x00000242: "CKM_RIPEMD160_HMAC_GENERAL",
    0x00000250: "CKM_SHA256",
    0x00000251: "CKM_SHA256_HMAC",
    0x00000252: "CKM_SHA256_HMAC_GENERAL",
    0x00000255: "CKM_SHA224",
    0x00000256: "CKM_SHA224_HMAC",
    0x00000257: "CKM_SHA224_HMAC_GENERAL",
    0x00000260: "CKM_SHA384",
    0x00000261: "CKM_SHA384_HMAC",
    0x00000262: "CKM_SHA384_HMAC_GENERAL",
    0x00000270: "CKM_SHA512",
    0x00000271: "CKM_SHA512_HMAC",
    0x00000272: "CKM_SHA512_HMAC_GENERAL",
    0x00000280: "CKM_SECURID_KEY_GEN",
    0x00000282: "CKM_SECURID",
    0x00000290: "CKM_HOTP_KEY_GEN",
    0x00000291: "CKM_HOTP",
    0x000002A0: "CKM_ACTI",
    0x000002A1: "CKM_ACTI_KEY_GEN",
    0x00000300: "CKM_CAST_KEY_GEN",
    0x00000301: "CKM_CAST_ECB",
    0x00000302: "CKM_CAST_CBC",
    0x00000303: "CKM_CAST_MAC",
    0x00000304: "CKM_CAST_MAC_GENERAL",
    0x00000305: "CKM_CAST_CBC_PAD",
    0x00000310: "CKM_CAST3_KEY_GEN",
    0x00000311: "CKM_CAST3_ECB",
    0x00000312: "CKM_CAST3_CBC",
    0x00000313: "CKM_CAST3_MAC",
    0x00000314: "CKM_CAST3_MAC_GENERAL",
    0x00000315: "CKM_CAST3_CBC_PAD",
    0x00000320: "CKM_CAST_KEY_GEN",  # Note: each of these could be CAST5 or CAST128
    0x00000321: "CKM_CAST_ECB",
    0x00000322: "CKM_CAST_CBC",
    0x00000323: "CKM_CAST_MAC",
    0x00000324: "CKM_CAST_MAC_GENERAL",
    0x00000325: "CKM_CAST_CBC_PAD",
    0x00000330: "CKM_RC5_KEY_GEN",
    0x00000331: "CKM_RC5_ECB",
    0x00000332: "CKM_RC5_CBC",
    0x00000333: "CKM_RC5_MAC",
    0x00000334: "CKM_RC5_MAC_GENERAL",
    0x00000335: "CKM_RC5_CBC_PAD",
    0x00000340: "CKM_IDEA_KEY_GEN",
    0x00000341: "CKM_IDEA_ECB",
    0x00000342: "CKM_IDEA_CBC",
    0x00000343: "CKM_IDEA_MAC",
    0x00000344: "CKM_IDEA_MAC_GENERAL",
    0x00000345: "CKM_IDEA_CBC_PAD",
    0x00000350: "CKM_GENERIC_SECRET_KEY_GEN",
    0x00000360: "CKM_CONCATENATE_BASE_AND_KEY",
    0x00000362: "CKM_CONCATENATE_BASE_AND_DATA",
    0x00000363: "CKM_CONCATENATE_DATA_AND_BASE",
    0x00000364: "CKM_XOR_BASE_AND_DATA",
    0x00000365: "CKM_EXTRACT_KEY_FROM_KEY",
    0x00000370: "CKM_SSL3_PRE_MASTER_KEY_GEN",
    0x00000371: "CKM_SSL3_MASTER_KEY_DERIVE",
    0x00000372: "CKM_SSL3_KEY_AND_MAC_DERIVE",
    0x00000373: "CKM_SSL3_MASTER_KEY_DERIVE_DH",
    0x00000374: "CKM_TLS_PRE_MASTER_KEY_GEN",
    0x00000375: "CKM_TLS_MASTER_KEY_DERIVE",
    0x00000376: "CKM_TLS_KEY_AND_MAC_DERIVE",
    0x00000377: "CKM_TLS_MASTER_KEY_DERIVE_DH",
    0x00000378: "CKM_TLS_PRF",
    0x00000380: "CKM_SSL3_MD5_MAC",
    0x00000381: "CKM_SSL3_SHA1_MAC",
    0x00000390: "CKM_MD5_KEY_DERIVATION",
    0x00000391: "CKM_MD2_KEY_DERIVATION",
    0x00000392: "CKM_SHA1_KEY_DERIVATION",
    0x00000393: "CKM_SHA256_KEY_DERIVATION",
    0x00000394: "CKM_SHA384_KEY_DERIVATION",
    0x00000395: "CKM_SHA512_KEY_DERIVATION",
    0x00000396: "CKM_SHA224_KEY_DERIVATION",
    0x000003A0: "CKM_PBE_MD2_DES_CBC",
    0x000003A1: "CKM_PBE_MD5_DES_CBC",
    0x000003A2: "CKM_PBE_MD5_CAST_CBC",
    0x000003A3: "CKM_PBE_MD5_CAST3_CBC",
    0x000003A4: "CKM_PBE_HASH_CAST5_CBC",  # Note, HASH could be MD5, SHA1, etc
    0x000003A6: "CKM_PBE_SHA1_RC4_128",
    0x000003A7: "CKM_PBE_SHA1_RC4_40",
    0x000003A8: "CKM_PBE_SHA1_DES3_EDE_CBC",
    0x000003A9: "CKM_PBE_SHA1_DES2_EDE_CBC",
    0x000003AA: "CKM_PBE_SHA1_RC2_128_CBC",
    0x000003AB: "CKM_PBE_SHA1_RC2_40_CBC",
    0x000003B0: "CKM_PKCS5_PBKD2",
    0x000003C0: "CKM_PBA_SHA1_WITH_SHA1_HMAC",
    0x000003D0: "CKM_WTLS_PRE_MASTER_KEY_GEN",
    0x000003D1: "CKM_WTLS_MASTER_KEY_DERIVE",
    0x000003D2: "CKM_WTLS_MASTER_KEY_DERIVE_DH_ECC",
    0x000003D3: "CKM_WTLS_PRF",
    0x000003D4: "CKM_WTLS_SERVER_KEY_AND_MAC_DERIVE",
    0x000003D5: "CKM_WTLS_CLIENT_KEY_AND_MAC_DERIVE",
    0x00000400: "CKM_KEY_WRAP_LYNKS",
    0x00000401: "CKM_KEY_WRAP_SET_OAEP",
    0x00000500: "CKM_CMS_SIG",
    0x00000510: "CKM_KIP_DERIVE",
    0x00000511: "CKM_KIP_WRAP",
    0x00000512: "CKM_KIP_MAC",
    0x00000550: "CKM_CAMELLIA_KEY_GEN",
    0x00000551: "CKM_CAMELLIA_ECB",
    0x00000552: "CKM_CAMELLIA_CBC",
    0x00000553: "CKM_CAMELLIA_MAC",
    0x00000554: "CKM_CAMELLIA_MAC_GENERAL",
    0x00000555: "CKM_CAMELLIA_CBC_PAD",
    0x00000556: "CKM_CAMELLIA_ECB_ENCRYPT_DATA",
    0x00000557: "CKM_CAMELLIA_CBC_ENCRYPT_DATA",
    0x00000558: "CKM_CAMELLIA_CTR",
    0x00000560: "CKM_ARIA_KEY_GEN",
    0x00000561: "CKM_ARIA_ECB",
    0x00000562: "CKM_ARIA_CBC",
    0x00000563: "CKM_ARIA_MAC",
    0x00000564: "CKM_ARIA_MAC_GENERAL",
    0x00000565: "CKM_ARIA_CBC_PAD",
    0x00000566: "CKM_ARIA_ECB_ENCRYPT_DATA",
    0x00000567: "CKM_ARIA_CBC_ENCRYPT_DATA",
    0x00001000: "CKM_SKIPJACK_KEY_GEN",
    0x00001001: "CKM_SKIPJACK_ECB64",
    0x00001002: "CKM_SKIPJACK_CBC64",
    0x00001003: "CKM_SKIPJACK_OFB64",
    0x00001004: "CKM_SKIPJACK_CFB64",
    0x00001005: "CKM_SKIPJACK_CFB32",
    0x00001006: "CKM_SKIPJACK_CFB16",
    0x00001007: "CKM_SKIPJACK_CFB8",
    0x00001008: "CKM_SKIPJACK_WRAP",
    0x00001009: "CKM_SKIPJACK_PRIVATE_WRAP",
    0x0000100a: "CKM_SKIPJACK_RELAYX",
    0x00001010: "CKM_KEA_KEY_PAIR_GEN",
    0x00001011: "CKM_KEA_KEY_DERIVE",
    0x00001020: "CKM_FORTEZZA_TIMESTAMP",
    0x00001030: "CKM_BATON_KEY_GEN",
    0x00001031: "CKM_BATON_ECB128",
    0x00001032: "CKM_BATON_ECB96",
    0x00001033: "CKM_BATON_CBC128",
    0x00001034: "CKM_BATON_COUNTER",
    0x00001035: "CKM_BATON_SHUFFLE",
    0x00001036: "CKM_BATON_WRAP",
    0x00001040: "CKM_EC_KEY_PAIR_GEN",
    0x00001041: "CKM_ECDSA",
    0x00001042: "CKM_ECDSA_SHA1",
    0x00001050: "CKM_ECDH1_DERIVE",
    0x00001051: "CKM_ECDH1_COFACTOR_DERIVE",
    0x00001052: "CKM_ECMQV_DERIVE",
    0x00001060: "CKM_JUNIPER_KEY_GEN",
    0x00001061: "CKM_JUNIPER_ECB128",
    0x00001062: "CKM_JUNIPER_CBC128",
    0x00001063: "CKM_JUNIPER_COUNTER",
    0x00001064: "CKM_JUNIPER_SHUFFLE",
    0x00001065: "CKM_JUNIPER_WRAP",
    0x00001070: "CKM_FASTHASH",
    0x00001080: "CKM_AES_KEY_GEN",
    0x00001081: "CKM_AES_ECB",
    0x00001082: "CKM_AES_CBC",
    0x00001083: "CKM_AES_MAC",
    0x00001084: "CKM_AES_MAC_GENERAL",
    0x00001085: "CKM_AES_CBC_PAD",
    0x00001086: "CKM_AES_CTR",
    0x00001089: "CKM_AES_CMAC_GENERAL",
    0x0000108A: "CKM_AES_CMAC",
    0x00001090: "CKM_BLOWFISH_KEY_GEN",
    0x00001091: "CKM_BLOWFISH_CBC",
    0x00001092: "CKM_TWOFISH_KEY_GEN",
    0x00001093: "CKM_TWOFISH_CBC",
    0x00001100: "CKM_DES_ECB_ENCRYPT_DATA",
    0x00001101: "CKM_DES_CBC_ENCRYPT_DATA",
    0x00001102: "CKM_DES3_ECB_ENCRYPT_DATA",
    0x00001103: "CKM_DES3_CBC_ENCRYPT_DATA",
    0x00001104: "CKM_AES_ECB_ENCRYPT_DATA",
    0x00001105: "CKM_AES_CBC_ENCRYPT_DATA",
    0x00002000: "CKM_DSA_PARAMETER_GEN",
    0x00002001: "CKM_DH_PKCS_PARAMETER_GEN",
    0x00002002: "CKM_X9_42_DH_PARAMETER_GEN",
    0x00002109: "CKM_AES_KEY_WRAP",
    0x0000210A: "CKM_AES_KEY_WRAP_PAD",
    0x80000000: "CKM_VENDOR_DEFINED",
    0x00008000: "CKM_VENDOR_DEFINED_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 0: "CKM_CAST_KEY_GEN_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 1: "CKM_CAST_ECB_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 2: "CKM_CAST_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 3: "CKM_CAST_MAC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 4: "CKM_CAST3_KEY_GEN_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 5: "CKM_CAST3_ECB_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 6: "CKM_CAST3_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 7: "CKM_CAST3_MAC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 8: "CKM_PBE_MD2_DES_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 9: "CKM_PBE_MD5_DES_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 10: "CKM_PBE_MD5_CAST_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 11: "CKM_PBE_MD5_CAST3_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 12: "CKM_CONCATENATE_BASE_AND_KEY_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 13: "CKM_CONCATENATE_KEY_AND_BASE_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 14: "CKM_CONCATENATE_BASE_AND_DATA_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 15: "CKM_CONCATENATE_DATA_AND_BASE_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 16: "CKM_XOR_BASE_AND_DATA_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 17: "CKM_EXTRACT_KEY_FROM_KEY_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 18: "CKM_MD5_KEY_DERIVATION_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 19: "CKM_MD2_KEY_DERIVATION_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 20: "CKM_SHA1_KEY_DERIVATION_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 21: "CKM_GENERIC_SECRET_KEY_GEN_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 22: "CKM_CAST5_KEY_GEN_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 23: "CKM_CAST5_ECB_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 24: "CKM_CAST5_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 25: "CKM_CAST5_MAC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 26: "CKM_PBE_SHA1_CAST5_CBC_OLD_XXX",
    CKM_VENDOR_DEFINED_OLD_XXX + 27: "CKM_KEY_TRANSLATION",
    CKM_VENDOR_DEFINED + 27: "CKM_XOR_BASE_AND_KEY",
    CKM_VENDOR_DEFINED_OLD_XXX + 28: "CKM_2DES_KEY_DERIVATION",
    CKM_VENDOR_DEFINED_OLD_XXX + 29: "CKM_INDIRECT_LOGIN_REENCRYPT",
    CKM_VENDOR_DEFINED_OLD_XXX + 30: "CKM_PBE_SHA1_DES3_EDE_CBC_OLD",
    CKM_VENDOR_DEFINED_OLD_XXX + 31: "CKM_PBE_SHA1_DES2_EDE_CBC_OLD",
    (CKM_VENDOR_DEFINED + 0x100): "CKM_HAS160",
    (CKM_VENDOR_DEFINED + 0x101): "CKM_KCDSA_KEY_PAIR_GEN",
    (CKM_VENDOR_DEFINED + 0x102): "CKM_KCDSA_HAS160",
    (CKM_VENDOR_DEFINED + 0x103): "CKM_SEED_KEY_GEN",
    (CKM_VENDOR_DEFINED + 0x104): "CKM_SEED_ECB",
    (CKM_VENDOR_DEFINED + 0x105): "CKM_SEED_CBC",
    (CKM_VENDOR_DEFINED + 0x106): "CKM_SEED_CBC_PAD",
    (CKM_VENDOR_DEFINED + 0x107): "CKM_SEED_MAC",
    (CKM_VENDOR_DEFINED + 0x108): "CKM_SEED_MAC_GENERAL",
    (CKM_VENDOR_DEFINED + 0x109): "CKM_KCDSA_SHA1",
    (CKM_VENDOR_DEFINED + 0x10A): "CKM_KCDSA_SHA224",
    (CKM_VENDOR_DEFINED + 0x10B): "CKM_KCDSA_SHA256",
    (CKM_VENDOR_DEFINED + 0x10C): "CKM_KCDSA_SHA384",
    (CKM_VENDOR_DEFINED + 0x10D): "CKM_KCDSA_SHA512",
    (CKM_VENDOR_DEFINED + 0x10F): "CKM_KCDSA_PARAMETER_GEN",
    (CKM_VENDOR_DEFINED + 0x110): "CKM_SHA224_RSA_PKCS_OLD",
    (CKM_VENDOR_DEFINED + 0x111): "CKM_SHA224_RSA_PKCS_PSS_OLD",
    (CKM_VENDOR_DEFINED + 0x112): "CKM_SHA224_OLD",
    (CKM_VENDOR_DEFINED + 0x113): "CKM_SHA224_HMAC_OLD",
    (CKM_VENDOR_DEFINED + 0x114): "CKM_SHA224_HMAC_GENERAL_OLD",
    (CKM_VENDOR_DEFINED + 0x115): "CKM_SHA224_KEY_DERIVATION_OLD",
    (CKM_VENDOR_DEFINED + 0x116): "CKM_DES3_CTR",
    (CKM_VENDOR_DEFINED + 0x118): "CKM_AES_CFB8",
    (CKM_VENDOR_DEFINED + 0x119): "CKM_AES_CFB128",
    (CKM_VENDOR_DEFINED + 0x11a): "CKM_AES_OFB",
    0x00001087: "CKM_AES_GCM",  # Used to be vendor defined + 0x11c
    (CKM_VENDOR_DEFINED + 0x11d): "CKM_ARIA_CFB8",
    (CKM_VENDOR_DEFINED + 0x11e): "CKM_ARIA_CFB128",
    (CKM_VENDOR_DEFINED + 0x11f): "CKM_ARIA_OFB",
    (CKM_VENDOR_DEFINED + 0x120): "CKM_ARIA_CTR",
    (CKM_VENDOR_DEFINED + 0x121): "CKM_ARIA_GCM",
    (CKM_VENDOR_DEFINED + 0x122): "CKM_ECDSA_SHA224",
    (CKM_VENDOR_DEFINED + 0x123): "CKM_ECDSA_SHA256",
    (CKM_VENDOR_DEFINED + 0x124): "CKM_ECDSA_SHA384",
    (CKM_VENDOR_DEFINED + 0x125): "CKM_ECDSA_SHA512",
    (CKM_VENDOR_DEFINED + 0x126): "CKM_AES_GMAC",
    (CKM_VENDOR_DEFINED + 0x128): "CKM_ARIA_CMAC",
    (CKM_VENDOR_DEFINED + 0x129): "CKM_ARIA_CMAC_GENERAL",
    (CKM_VENDOR_DEFINED + 0x12c): "CKM_SEED_CMAC",
    (CKM_VENDOR_DEFINED + 0x12d): "CKM_SEED_CMAC_GENERAL",
    (CKM_VENDOR_DEFINED + 0x12e): "CKM_DES3_CBC_PAD_IPSEC",
    (CKM_VENDOR_DEFINED + 0x12f): "CKM_AES_CBC_PAD_IPSEC",
    (CKM_VENDOR_DEFINED + 0x130): "CKM_ARIA_L_ECB",
    (CKM_VENDOR_DEFINED + 0x131): "CKM_ARIA_L_CBC",
    (CKM_VENDOR_DEFINED + 0x132): "CKM_ARIA_L_CBC_PAD",
    (CKM_VENDOR_DEFINED + 0x133): "CKM_ARIA_L_MAC",
    (CKM_VENDOR_DEFINED + 0x134): "CKM_ARIA_L_MAC_GENERAL",
    (CKM_VENDOR_DEFINED + 0x135): "CKM_SHA224_RSA_X9_31",
    (CKM_VENDOR_DEFINED + 0x136): "CKM_SHA256_RSA_X9_31",
    (CKM_VENDOR_DEFINED + 0x137): "CKM_SHA384_RSA_X9_31",
    (CKM_VENDOR_DEFINED + 0x138): "CKM_SHA512_RSA_X9_31",
    (CKM_VENDOR_DEFINED + 0x139): "CKM_SHA1_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x13a): "CKM_SHA224_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x13b): "CKM_SHA256_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x13c): "CKM_SHA384_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x13d): "CKM_SHA512_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x13e): "CKM_RSA_X9_31_NON_FIPS",
    (CKM_VENDOR_DEFINED + 0x140): "CKM_DSA_SHA224",
    (CKM_VENDOR_DEFINED + 0x141): "CKM_DSA_SHA256",
    (CKM_VENDOR_DEFINED + 0x142): "CKM_RSA_FIPS_186_3_AUX_PRIME_KEY_PAIR_GEN",
    (CKM_VENDOR_DEFINED + 0x143): "CKM_RSA_FIPS_186_3_PRIME_KEY_PAIR_GEN",
    (CKM_VENDOR_DEFINED + 0x144): "CKM_SEED_CTR",
    (CKM_VENDOR_DEFINED + 0x145): "CKM_KCDSA_HAS160_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x146): "CKM_KCDSA_SHA1_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x147): "CKM_KCDSA_SHA224_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x148): "CKM_KCDSA_SHA256_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x149): "CKM_KCDSA_SHA384_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x151): "CKM_KCDSA_SHA512_NO_PAD",
    (CKM_VENDOR_DEFINED + 0x150): "CKM_DES3_X919_MAC",
    (CKM_VENDOR_DEFINED + 0x160): "CKM_ECDSA_KEY_PAIR_GEN_W_EXTRA_BITS",
    (CKM_VENDOR_DEFINED + 0x161): "CKM_ECDSA_GBCS_SHA256",
    (CKM_VENDOR_DEFINED + 0x170): "CKM_AES_KW",
    (CKM_VENDOR_DEFINED + 0x171): "CKM_AES_KWP",
    (CKM_VENDOR_DEFINED + 0x172): "CKM_TDEA_KW",
    (CKM_VENDOR_DEFINED + 0x173): "CKM_TDEA_KWP",
    (CKM_VENDOR_DEFINED + 0x200): "CKM_AES_CBC_PAD_EXTRACT",
    (CKM_VENDOR_DEFINED + 0x201): "CKM_AES_CBC_PAD_INSERT",
    (CKM_VENDOR_DEFINED + 0x202): "CKM_AES_CBC_PAD_EXTRACT_FLATTENED",
    (CKM_VENDOR_DEFINED + 0x203): "CKM_AES_CBC_PAD_INSERT_FLATTENED",
    (CKM_VENDOR_DEFINED + 0x204): "CKM_AES_CBC_PAD_EXTRACT_DOMAIN_CTRL",
    (CKM_VENDOR_DEFINED + 0x205): "CKM_AES_CBC_PAD_INSERT_DOMAIN_CTRL",
    (CKM_VENDOR_DEFINED + 0x502): "CKM_PLACE_HOLDER_FOR_ERACOME_DEF_IN_SHIM",
    (CKM_VENDOR_DEFINED + 0x611): "CKM_DES2_DUKPT_PIN",
    (CKM_VENDOR_DEFINED + 0x612): "CKM_DES2_DUKPT_MAC",
    (CKM_VENDOR_DEFINED + 0x613): "CKM_DES2_DUKPT_MAC_RESP",
    (CKM_VENDOR_DEFINED + 0x614): "CKM_DES2_DUKPT_DATA",
    (CKM_VENDOR_DEFINED + 0x615): "CKM_DES2_DUKPT_DATA_RESP",
    (CKM_VENDOR_DEFINED + 0xA00): "CKM_ECIES",
    (CKM_VENDOR_DEFINED + 0xA01): "CKM_XOR_BASE_AND_DATA_W_KDF",
    (CKM_VENDOR_DEFINED + 0xA02): "CKM_NIST_PRF_KDF",
    (CKM_VENDOR_DEFINED + 0xA03): "CKM_PRF_KDF",
    (CKM_VENDOR_DEFINED + 0xA04): "CKM_AES_XTS",
    (CKM_VENDOR_DEFINED + 0xB01): "CKM_SM3",
    (CKM_VENDOR_DEFINED + 0xB02): "CKM_SM3_HMAC",
    (CKM_VENDOR_DEFINED + 0xB03): "CKM_SM3_HMAC_GENERAL",
    (CKM_VENDOR_DEFINED + 0xB04): "CKM_SM3_KEY_DERIVATION"
}
