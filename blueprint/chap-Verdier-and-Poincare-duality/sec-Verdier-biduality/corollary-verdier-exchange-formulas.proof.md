+++
kind = "proof"
of = "corollary-verdier-exchange-formulas"
order = 849
uses = ["proposition-exact-products", "proposition-milnor-sequence", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-pro-etale-base-change-map", "definition-projection-formula-map", "proposition-proper-direct-image-constructible-complexes", "proposition-composition-base-change-rf-shriek", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-dctf", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "lemma-internal-adjunction-two-exchange-formulas", "lemma-verdier-duality-preserves-constructibility", "theorem-verdier-biduality"]
+++
Two of the formulas are Lemma [lemma-internal-adjunction-two-exchange-formulas], and we obtain the other two by applying these to the [Verdier dual](@definition-verdier-dual-evaluation) of the argument and
using [biduality](@theorem-verdier-biduality) on both schemes. Explicitly, for $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)}$ and
$L\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)}$ this reads

$$
\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}Rf_*K\simeq\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}Rf_*\href{@definition-verdier-dual-evaluation}{\mathbb D_X}(\href{@definition-verdier-dual-evaluation}{\mathbb D_XK})
\simeq\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}\href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@definition-verdier-dual-evaluation}{\mathbb D_XK},
$$

$$
\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\href{@theorem-existence-exceptional-inverse-image}{f^!L}\simeq\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}(\href{@definition-verdier-dual-evaluation}{\mathbb D_YL})
\simeq\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\href{@definition-verdier-dual-evaluation}{\mathbb D_X}f^*\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\simeq f^*\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}.
$$

The formulas for $j$ and $i$ are the special cases $f=j$ and $f=i$.
