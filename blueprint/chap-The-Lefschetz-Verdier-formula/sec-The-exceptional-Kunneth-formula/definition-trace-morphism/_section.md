+++
id = "definition-trace-morphism"
kind = "definition"
title = "Trace morphism"
order = 914
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-correspondence", "lemma-external-duality-trace-morphism", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
In the setting of Lemma [lemma-external-duality-trace-morphism], let
$e_K:P_X\to R\Delta_{X*}\href{@definition-verdier-dual-evaluation}{\omega_X}$ be adjoint to the evaluation
$\Delta_X^*\href{@lemma-external-duality-trace-morphism}{P_X}=K\otimes^{\mathbf L} \href{@definition-verdier-dual-evaluation}{\mathbb D_XK}\to\href{@definition-verdier-dual-evaluation}{\omega_X}$. The
*trace morphism* is the composite

$$
\href{@lemma-external-duality-trace-morphism}{\mathcal H_c(K)}\simeq \href{@theorem-existence-exceptional-inverse-image}{c^!}\href{@lemma-external-duality-trace-morphism}{P_X}\xrightarrow{\href{@theorem-existence-exceptional-inverse-image}{c^!}e_K}\href{@theorem-existence-exceptional-inverse-image}{c^!}R\Delta_{X*}\href{@definition-verdier-dual-evaluation}{\omega_X}
\xrightarrow{\sim}Ri_{c*}\href{@theorem-existence-exceptional-inverse-image}{d_c^!}\href{@definition-verdier-dual-evaluation}{\omega_X}
\simeq Ri_{c*}\href{@definition-verdier-dual-evaluation}{\omega_{\Fix(c)}}
$$

of the second isomorphism of the lemma, $\href{@theorem-existence-exceptional-inverse-image}{c^!}e_K$, exceptional base
change for the proper map $\Delta_X$, and the composition of
[exceptional inverse images](@theorem-existence-exceptional-inverse-image) $\href{@theorem-existence-exceptional-inverse-image}{d_c^!}\href{@theorem-existence-exceptional-inverse-image}{a_X^!}=\href{@theorem-existence-exceptional-inverse-image}{a_{\Fix(c)}^!}$.
