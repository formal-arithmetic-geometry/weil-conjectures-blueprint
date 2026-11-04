+++
kind = "proof"
of = "proposition-proper-base-change-degree-zero"
order = 334
uses = ["lemma-sections-geometric-fibre"]
+++
We show that both stalks are the sections over the same geometric fibre.
Choose $\bar y':\operatorname{Spec}\Omega\to Y'$ and use the
composite $\bar y=g\bar y'$ as the geometric point of $Y$. Properness
is preserved by base change, so Lemma [lemma-sections-geometric-fibre]
applies to $f'$ as well as to $f$. The cartesian square identifies

$$
X'_{\bar y'}=X\times_Y\operatorname{Spec}\Omega=X_{\bar y}
$$

and identifies the two inverse image sheaves on it. Thus the stalks of
both sides of the desired map are the same set of sections. The underived
base change map sends a section
represented over $X\times_YV$ to its
restriction to the base change of the neighbourhood, and hence to its
restriction to this same fibre. In other words, the map on stalks is the
identity under the displayed identifications. Since geometric stalks detect
isomorphisms, this proves the assertion.
