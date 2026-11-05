+++
kind = "proof"
of = "proposition-relative-dualizing-complex"
order = 756
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
We define the isomorphism as a chain of three steps: restrict $\omega_f$ to
the diagonal of $X\times_YX$, move the diagonal to the zero section of
$T_{X/Y}$, and use the orientation of a vector bundle.

The projection $p_1$ is the base change of $f$ along $f$, so
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3) shows that
$\omega_{p_1}\simeq p_2^{*}\omega_f$. Since $p_2\circ\Delta$ is the
identity of $X$, we get the first isomorphism in

$$
\begin{aligned}
\omega_{f}
&\simeq L\Delta^{*}\omega_{p_1}
\xrightarrow{\sim}z^{*}\omega_{\pi}
\xrightarrow{\sim}z^{*}(\mathbf Z/\ell^n\mathbf Z)_{T_{X/Y}}(d)[2d]
\simeq(\mathbf Z/\ell^n\mathbf Z)_{X}(d)[2d].
\end{aligned}
$$

The second isomorphism is Lemma [lemma-section-normal-bundle] for the section
$\Delta$ of $p_1$, and the third is the inverse of the
isomorphism of Proposition [proposition-purity-vector-bundles]
at the constant sheaf, applied to the vector bundle $T_{X/Y}$ over $X$.
The last one holds because the pullback of a constant sheaf is constant.
Since each step is attached to $f$ without choices, the composite is
canonical.
