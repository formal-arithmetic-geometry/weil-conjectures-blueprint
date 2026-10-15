+++
kind = "proof"
of = "sk-prop-ctf-finite-proper"
uses = ["lem-fin-proper-bounded-constructible", "lem-amb-proper-coproducts", "sk-prop-ctf-finite-comparison", "sk-thm-properbasechange"]
+++
Work first on the étale site. Proper direct image of constructible torsion sheaves is constructible (Stacks,
Tag 0GL0), and $Rp_*$ has finite cohomological dimension (Stacks, Tag 0F10); together they give
$Rp_*C\in\Dbc(Y_{\mathrm{ét}},A)$ ([lem-fin-proper-bounded-constructible]). For finite Tor amplitude, suppose $C$
has Tor amplitude $[a,b]$, and choose a uniform bound $d$ for the $\ell$-cohomological dimensions of the
geometric fibers of $p$. For any $A$-module $N$, proper base change and the constant-module projection
formula (Stacks, Tag 0F12) in $\D(Y_{\mathrm{ét}},A)$ identify the stalk of $(Rp_*C)\otimes_A^{\mathbf L}N_Y$ at
$\bar y$ with

$$
R\Gamma\bigl(X_{\bar y},C|_{X_{\bar y}}\otimes_A^{\mathbf L}N_{X_{\bar y}}\bigr),
$$

which has cohomology only in $[a,b+d]$. Testing against constant modules suffices: a flat resolution of
$Rp_*C$ restricts at every geometric point to a flat resolution of the stalk, and tensoring with an
arbitrary sheaf is computed stalkwise. Thus $Rp_*C\in\Dctf(Y_{\mathrm{ét}},A)$ ([det-ctf-finite-proper-tor]).

On unbounded étale derived categories, proper direct image $Rp_*\colon\D(X_{\mathrm{ét}},A)\to\D(Y_{\mathrm{ét}},A)$
preserves all direct sums by Stacks, Tag 0F0D ([lem-amb-proper-coproducts], [lem-exc-direct-image-coproducts]),
and unbounded proper base change follows from the same uniform cohomological bound and the bounded below
theorem (equivalently Stacks, Tag 0F0C). The $A$-linear statements follow by forgetting coefficients, and
[sk-prop-ctf-finite-comparison] transfers them to the pro-étale localizing categories. Since $Rp_*$ preserves
the small subcategory and sums, it preserves its localizing closure. Finally, $j_!$ is exact, is a left
adjoint, and is stalkwise extension by zero, so it preserves constructibility, finite Tor amplitude and all
sums ([det-ctf-finite-proper-localizing]).

The comparison of compactifications and the composition isomorphisms ([sk-prop-sf-comp-coherence] and
[sk-thm-sf-comp-composition]) need only the base change and direct-sum assertions just proved.
