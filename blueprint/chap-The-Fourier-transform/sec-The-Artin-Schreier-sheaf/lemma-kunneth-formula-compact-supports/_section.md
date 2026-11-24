+++
id = "lemma-kunneth-formula-compact-supports"
kind = "lemma"
title = "Künneth formula for compact supports"
order = 1225
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
In this situation, let $K,L$ be bounded [constructible](@definition-constructible-sheaves) complexes with
coefficients in a field. Then the maps in

$$
\href{@proposition-construction-independence-rf-shriek}{Rh_!(p_1^*K\otimes p_2^*L)}
\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}(K\otimes \href{@proposition-construction-independence-rf-shriek}{Rp_{1!}p_2^*L})
\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}(K\otimes f^*\href{@proposition-construction-independence-rf-shriek}{Rg_!L})
\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!K}\otimes \href{@proposition-construction-independence-rf-shriek}{Rg_!L}
$$

of the projection formula for $p_1$, the [proper base change](@proposition-composition-base-change-rf-shriek) isomorphism
$\href{@proposition-construction-independence-rf-shriek}{Rp_{1!}p_2^*L}\to f^*\href{@proposition-construction-independence-rf-shriek}{Rg_!L}$ and the projection formula for $f$ are
isomorphisms. We call their composite
$\href{@proposition-construction-independence-rf-shriek}{Rh_!(K\boxtimes_SL)}\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!K}\otimes \href{@proposition-construction-independence-rf-shriek}{Rg_!L}$ the
*Künneth isomorphism*.
