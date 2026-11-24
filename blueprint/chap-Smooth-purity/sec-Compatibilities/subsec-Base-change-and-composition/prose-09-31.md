+++
id = "prose-09-31"
kind = "hidden"
title = "Base change and composition (2)"
order = 800
+++
**Composition.** For composition we again fix the composition
isomorphisms for [$f^!$](@theorem-existence-exceptional-inverse-image) with every coefficient ring before comparing the maps
[$\gamma$](@theorem-smooth-purity-all-admissible-coefficients). From now on, $g$ no longer denotes the base change in a square: let
$X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions
$d$ and $e$. Composing the finite adjunctions, we identify
[$(g\circ f)_A^!$](@theorem-existence-exceptional-inverse-image) with $\href{@theorem-existence-exceptional-inverse-image}{f_A^!}\href{@theorem-existence-exceptional-inverse-image}{g_A^!}$, compatibly with
$\href{@proposition-construction-independence-rf-shriek}{R(g\circ f)_{!,A}}\simeq \href{@proposition-construction-independence-rf-shriek}{Rg_{!,A}}\href{@proposition-construction-independence-rf-shriek}{Rf_{!,A}}$, and the counit of the
composite adjunction is the composite of the two counits.

The change-of-coefficients maps are compatible with composition: for $M\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)$ and
$K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Z_{\mathrm{pro}\acute{e}t}},A)$,

$$
b^{g\circ f}(M)=\href{@proposition-construction-independence-rf-shriek}{Rg_{!,B}(b^f(M))}\circ b^g(\href{@proposition-construction-independence-rf-shriek}{Rf_{!,A}M}),
\qquad
c^{g\circ f}(K)=\href{@theorem-existence-exceptional-inverse-image}{f_B^!}c^g(K)\circ c^f(\href{@theorem-existence-exceptional-inverse-image}{g_A^!K}).
$$

The first identity holds on each free term of a resolution of $B$ over $A$,
since the composition isomorphism is natural, and the totalization in
Lemma [lemma-sp-reduction] extends it to arbitrary $A\to B$. We get the
second by transposing under the composite adjunction.

On towers, the composition isomorphism for $Rf_{!,\bullet}$ is built from
the same constructions. The isomorphism
$\href{@proposition-sp-tower-geometric}{(g\circ f)^!_\bullet}\simeq \href{@proposition-sp-tower-geometric}{f^!_\bullet} \href{@proposition-sp-tower-geometric}{g^!_\bullet}$ is the isomorphism of
right adjoints given by the composite adjunction on towers. Since evaluation at
level $n$ carries the counits on towers to the finite counits
(Proposition [proposition-sp-tower-geometric]), the level $n$ of
these isomorphisms is the finite one, and by the identities above they commute
with the transition maps, which are built from $b$ and $c$. Applying
$R\varprojlim$ gives the integral composition isomorphisms

$$
\href{@proposition-construction-independence-rf-shriek}{R(g\circ f)_{!,\mathcal O_E}}\simeq \href{@proposition-construction-independence-rf-shriek}{Rg_{!,\mathcal O_E}}\href{@proposition-construction-independence-rf-shriek}{Rf_{!,\mathcal O_E}},
\qquad
\href{@theorem-existence-exceptional-inverse-image}{(g\circ f)_{\mathcal O_E}^{!}}\simeq \href{@theorem-existence-exceptional-inverse-image}{f_{\mathcal O_E}^{!}}\href{@theorem-existence-exceptional-inverse-image}{g_{\mathcal O_E}^{!}},
$$

between [$\Dbc(X,\mathcal O_E)$](@definition-constructible-sheaves) and [$\Dbc(Z,\mathcal O_E)$](@definition-constructible-sheaves); for $E=\mathbf Q_\ell$ the
coefficients are $\mathbf Z_\ell$. As for base change, inverting $\ell$ and extending
scalars give the composition isomorphisms with coefficients $E$ and $\overline{\mathbf Q}_\ell$.
These isomorphisms $\href{@theorem-existence-exceptional-inverse-image}{(g\circ f)^!}\simeq \href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!}$ are the composition isomorphisms of
Proposition [proposition-composition-open-restriction-compactifications-f](1).
Indeed, the isomorphism of that proposition is characterized by the following
property: it carries the counit of $\href{@proposition-construction-independence-rf-shriek}{R(g\circ f)_!}\dashv\href{@theorem-existence-exceptional-inverse-image}{(g\circ f)^!}$,
composed with the composition isomorphism for [$Rf_!$](@proposition-construction-independence-rf-shriek), to the composite of
the counits for $f$ and $g$. By [uniqueness of adjoints](@proposition-sp-unique-adjoint) it therefore
suffices to check this property for every coefficient ring. With finite
coefficients it holds by definition. On towers the composition isomorphism
is the one of the composite adjunction, so in $D(\operatorname{Tow})$ it
carries the counit on towers of $g\circ f$ to the composite of the counits
on towers. By the comparison following the construction of $e_{f,\bullet}$
in Subsection [subsec-Base-change-and-composition], [$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation) carries the counits
and the composition isomorphism for [$Rf_!$](@proposition-construction-independence-rf-shriek) with coefficients $\mathcal O_E$
to those on towers, and applying $R\varprojlim$ gives the property over
$\mathcal O_E$. Similarly, the same comparison shows that extension of scalars along
$\mathcal O_E\to E$ and $E\to\overline{\mathbf Q}_\ell$ carries the counits and the
composition isomorphisms for [$Rf_!$](@proposition-construction-independence-rf-shriek) to the corresponding ones, which gives
the property over $E$ and $\overline{\mathbf Q}_\ell$.

With these composition isomorphisms in place for every coefficient ring,
the statement takes the following form. In topological terms it says that
the orientation of a composite of submersions is the product of the
orientations.
