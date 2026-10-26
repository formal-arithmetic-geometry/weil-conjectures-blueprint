+++
id = "lem-pur-kunneth-supported"
kind = "lemma"
title = "Kunneth for cohomology with closed support"
order = 2897
uses = ["def-kun-derived-tensor", "def-kun-tor-amplitude", "def-pur-support-cohomology", "def-pur-supported-exterior-product", "def-weil-finite-field-fiber", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-origin-witness", "def-weil-scheme-morphism-properties", "lem-kun-kunneth-map-natural", "lem-pur-ordinary-kunneth-finite-ring", "lem-pur-support-restriction-triangle", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "thm-weil-pbc-site-comparison"]
+++
Let $k$ be the algebraically closed field of
[def-weil-finite-field-fiber], put
$A=\mathcal O_E/\pi_E^n$, and let $Z\subset X,W\subset Y$
be closed subschemes of
separated finite-type
$k$-schemes.
Let $K\in D^b(X_{\mathrm{et}},A)$ and
$L\in D^b(Y_{\mathrm{et}},A)$ be
bounded complexes,
with $L$ of
finite Tor amplitude.
Then the supported
exterior product is an isomorphism:

$$
\kappa^{Z,W}_{K,L}:
R\Gamma_Z(X,K)\otimes_A^LR\Gamma_W(Y,L)
\xrightarrow{\ \sim\ }
R\Gamma_{Z\times W}(X\times_kY,K\boxtimes_A^L L).
$$

Here $R\Gamma_Z,R\Gamma_W$ are the
derived support functors.
The assertion also holds for the pro-etale realizations of these
complexes equipped with
etale-origin witnesses.
