+++
kind = "proof"
of = "theorem-existence-exceptional-inverse-image"
order = 527
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "proposition-ctf-equals-bc", "lemma-descent-finite-coefficient-field", "lemma-cohomology-modules-underlying-abelian", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-proper-direct-image-finite-coefficients", "proposition-proper-base-change-complete-integral", "proposition-proper-direct-image-constructible-complexes", "proposition-ind-constructible-sheaves", "proposition-comparison-etale-derived-category", "corollary-proper-direct-image-finite-coefficients-localizing", "lemma-proper-direct-image-unbounded-complexes", "lemma-hypotheses-brown-representability", "proposition-six-operations-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
We construct $f^!N$ one object at a time as the object representing
maps out of $Rf_!(-)$ into $N$, and then check direct sums on the compact
generators.

For $N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$, the functor

$$
\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))^{\mathrm{op}}\longrightarrow\operatorname{Ab},
\qquad M\longmapsto\Hom(Rf_!M,N)
$$

is cohomological and sends direct sums to products. By
Lemma [lemma-hypotheses-brown-representability], $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ is
compactly generated, and Brown representability [Stacks, [0A8F](https://stacks.math.columbia.edu/tag/0A8F)] says
that on such a category every cohomological functor sending direct sums
to products is representable, say by $f^!N$. By the
Yoneda lemma, these objects form a right adjoint, and a right adjoint of an
exact functor of triangulated categories is exact [Stacks, [0A8G](https://stacks.math.columbia.edu/tag/0A8G)].

To see that $f^!$ preserves direct sums, we test the canonical map
$\bigoplus_\alpha f^!N_\alpha\to f^!(\bigoplus_\alpha N_\alpha)$
on a compact generator $G\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and its shifts.
On the source, compactness of $G$ and adjunction give

$$
\Hom\Bigl(G[n],\bigoplus_\alpha f^!N_\alpha\Bigr)
=\bigoplus_\alpha\Hom(G[n],f^!N_\alpha)
=\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha).
$$

On the target, adjunction and compactness of $Rf_!G\in D^b_{\mathrm{ctf}}(Y,\Lambda)$
give the same group. The map therefore induces bijections on
$\Hom(G[n],-)$ for all compact generators $G$ and all $n$. Applying the
detection property to its cone, we see that it is an isomorphism.
