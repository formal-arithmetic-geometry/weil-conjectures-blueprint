+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--3"
order = 830006
uses = ["definition-derived-base-change-map", "proposition-exceptional-inverse-image-smooth-morphism", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--1", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--14", "proposition-six-operations-dctf--15", "proposition-sp-unique-adjoint--1", "definition-verdier-dual-evaluation--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
For (10.4), note that both $f^!\mathbb D_YL$ and
$\mathbb D_Xf^*L$ lie in $D^b_{\mathrm{ctf}}(X,\Lambda)$. Since tensoring with
$f^*L$ preserves $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, we may test on objects $M$
of this category:

$$
\begin{aligned}
\Hom_X(M,f^!\mathbb D_YL)
&\simeq\Hom_Y(Rf_!M,\cHom_Y(L,\omega_Y))\\
&\simeq\Hom_Y(Rf_!M\otimes^{\mathbf L}L,\omega_Y)\\
&\simeq\Hom_X(M\otimes^{\mathbf L}f^*L,f^!\omega_Y)\\
&\simeq\Hom_X(M,\mathbb D_Xf^*L).
\end{aligned}
$$

Again, the bijection is induced by the map defined before the lemma, and by Yoneda
we get (10.4).

*Source:* the proof of Lemma [lemma-internal-adjunction-two-exchange-formulas].
