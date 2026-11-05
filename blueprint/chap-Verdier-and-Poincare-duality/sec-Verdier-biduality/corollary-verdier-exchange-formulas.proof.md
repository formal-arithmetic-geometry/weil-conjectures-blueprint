+++
kind = "proof"
of = "corollary-verdier-exchange-formulas"
order = 849
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "lemma-verdier-duality-preserves-constructibility", "theorem-verdier-biduality", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Two of the formulas are Lemma [lemma-internal-adjunction-two-exchange-formulas], and we obtain the other two by applying these to the Verdier dual of the argument and
using biduality on both schemes. Explicitly, for $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ this reads

$$
\mathbb D_YRf_*K\simeq\mathbb D_YRf_*\mathbb D_X(\mathbb D_XK)
\simeq\mathbb D_Y\mathbb D_YRf_!\mathbb D_XK\simeq Rf_!\mathbb D_XK,
$$

$$
\mathbb D_Xf^!L\simeq\mathbb D_Xf^!\mathbb D_Y(\mathbb D_YL)
\simeq\mathbb D_X\mathbb D_Xf^*\mathbb D_YL\simeq f^*\mathbb D_YL.
$$

The formulas for $j$ and $i$ are the special cases $f=j$ and $f=i$.
