+++
kind = "proof"
of = "lem-weil-pbc-normalization-comparison-on-iso-locus"
uses = ["lemma-constructible-pullback-constant", "lemma-weil-pbc-finite-exchange", "sbc-prop-extension-by-zero-and-arbitrary-base-change"]
+++
Form W = ν⁻¹(V) and T = U ×_X V. Finite base change identifies restriction of ν_*j′_!R with pushforward along ν_V of the restriction of j′_!R to W. Base change for extension by zero identifies the latter with extension by zero on U′ ×_X V. ([lemma-weil-pbc-finite-exchange], [sbc-prop-extension-by-zero-and-arbitrary-base-change]).

The Cartesian square and the isomorphism ν_V identify U′ ×_X V with T and identify the two open immersions and constant coefficients. Constant sheaf pullback preserves R. Pushforward along the isomorphism ν_V yields j_T!R; open base change also identifies the restricted source with j_T!R. Compose these isomorphisms. The argument holds for empty opens and zero R, and does not need density or finiteness of R. ([lemma-constructible-pullback-constant], [sbc-prop-extension-by-zero-and-arbitrary-base-change]).
