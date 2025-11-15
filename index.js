import * as jose from "jose"

async function exportPublicKey() {
  // IMPORTANT: Replace this placeholder with your actual Decoded JWK private key object as a string.
  const privateJwkString = `{
  "kty": "RSA",
  "key_ops": [
    "sign"
  ],
  "kid": "1ddc6a3d-1f0b-4d37-afd5-5fe7a2709d25",
  "d": "G-q1WT0DFWB8rtn0HfK5x7j8F9AkCCF7cSBusXG3eXF54NWeJWTPQuTCuQKpLBaFFuj3rKhdxYV6K5jm0PZzGiOu_fyGjh-n0qwxRiZzicwEQZB13f3uzHTzMcXsOzFlq5RdaZ9O4RxtDdJ02OTYdOdhq7Hk7a67ZQVG3x49-AmsoQRCyJnjNZfsbHRPd42phaiWxsOeXguScA2SR_EX38vnnocpiz6u2krWUBEAMBMBsvWcPp33TTgEHWxXRQdNGBI1PpdKvDCM5PqN7lgx1UfnHsJ5S8MTwgNKOmQKRmL9QTrJmy1CG8RtoDMmDkK2s838LryP8AekrGqEy5DLkQ",
  "n": "0bf3qiYoNpFfpKPyJYbbzV_GRhTFb8mkSZeHZCKJMIE2adwNeCnsRZr8S7-9wzCC6u60OM_URg1fOXzXy1Wv90dIAFaF406zL6fZGXZ7uRdNC8I-KiHx_B6CBEIka3Kz99fi1NOHWS-3_wvu9hKV0yg39j6yosrcE0UDxIW5heyXZ7wfFBBdRKinHlVeBLMnEpaVYr47seAn-A6Qm1JYhsgy4k5-wTJLbfki71qZF0L95-YDzaz56FwmwAupLHi1I6SO6eba_bOJtv8Cr1VMkx2UeOzvchzrrF-NEmK1cf8grXqchARxjfJFo_EiV25psKfL5VtKOdnBypcVX77MmoQ",
  "e": "AQAB",
  "p": "_Oy5cZkn00vu9FprOgJeDR36kkWrPCGCYQCnqBYs2QyWBebOkQHJz3rIYiyrA685pJ-VSlq1tdtXgVRLS3fMdkwKq2pMTI-v4H1hFpNz6L7AjpYxxYgm8X9_sB8Pz4ZfV6J9liky5R2C0gg1jUyMA-WFiv_1fISjk3h1AZjuhBs",
  "q": "1ETBigHBVymUbjSxVROrz8r-8tEtnBizenrupBZXuKNo9UlZyTw2vULM8bI0Ww-ugAYER2TvsuliC4ISQ4Res0CibNT9Q97HtxbypxzvsH9ZBlwJFam-tZAceaRVA7Z1egW2qzfrImX_DD5ZPraTyEde0yJ-RICi4lAGSfS_LVU_M",
  "dp": "BwUfBIsmstOptziHP13vdFe_q62pWgroDn8xKBYtenzB8Tn9w8KT8mFLDIaG3JxRckNHpn-sCXckD5_iUx7pGuNzbFyP75QRYp64QiMnlW8t8wej3AKyagOK7L1_99eX79u_tppAImHWTrQRoHFedYE6WqhODP21eJNgVAIFpL8",
  "dq": "02-pWM5mx2ujbiMOgLAXc-PAEB5MUDBKyvCMM4nbIn2iw2Qzy3Sc5AVoArpqjYKK3VlUf1e0D9aHknuBkiO2smX0HJBNHkHXu-OLeaCTTQeIU0h1-Nl0z1EDWgeRJF8kW-rs4EaT8vzgJM4yr6CYUN70FshM-db9BGc2RXCdDgE",
  "qi": "LmzoWro-QxzmqH5P6h6-XaKsdaLd_eMN32mpdj3yTMqM4_iSSw53ymSqJrVKaq-9xmyMuXMRsdyW7F6cQANxZtfdyAQazEZMimk_kN-BIP2knsxGrxzDgggSFTcZktYXDKQW1PLom2jbH4Yqc7U5CsCzAQFyodKck7E9Vk5ScX0"
}`

  try {
    const privateJwkObject = JSON.parse(privateJwkString)

    // Construct a public JWK object from the private JWK's public parameters
    const publicJwkObject = {
      kty: privateJwkObject.kty,
      n: privateJwkObject.n,
      e: privateJwkObject.e,
      kid: privateJwkObject.kid, // Include kid if present and desired for public key
    }

    // Import the public JWK to get a CryptoKey object for the public key
    const publicKey = await jose.importJWK(publicJwkObject, "RS256", { extractable: true })

    // Now export the public key in desired formats
    const exportedPublicJwk = await jose.exportJWK(publicKey) // Export public key in JWK format
    const publicPem = await jose.exportSPKI(publicKey) // Export public key in SPKI PEM format

    console.log("--- Public Key (JWK Format) ---")
    console.log(JSON.stringify(exportedPublicJwk, null, 2))
    console.log("-------------------------------")

    console.log("--- Public Key (PEM Format) ---")
    console.log(publicPem)
    console.log("-------------------------------")
  } catch (error) {
    console.error("Error exporting public key:", error)
  }
}

exportPublicKey()
