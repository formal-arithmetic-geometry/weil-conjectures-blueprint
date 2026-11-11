+++
kind = "proof"
of = "corollary-verdier-exchange-formulas"
order = 849
uses = ["proposition-exact-products", "proposition-milnor-sequence", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-pro-etale-base-change-map", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "proposition-composition-base-change-rf-shriek", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "lemma-internal-adjunction-two-exchange-formulas", "lemma-verdier-duality-preserves-constructibility", "theorem-verdier-biduality"]
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
