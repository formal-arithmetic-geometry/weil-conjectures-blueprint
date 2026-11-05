+++
id = "prose-09-31"
kind = "hidden"
title = "Base change and composition (2)"
order = 800
+++
**Composition.** For composition we again fix the composition
isomorphisms for $f^!$ with every coefficient ring before comparing the maps
$\gamma$. From now on, $g$ no longer denotes the base change in a square: let
$X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions
$d$ and $e$. Composing the finite adjunctions, we identify
$(g\circ f)_A^!$ with $f_A^!g_A^!$, compatibly with
$R(g\circ f)_{!,A}\simeq Rg_{!,A}Rf_{!,A}$, and the counit of the
composite adjunction is the composite of the two counits.

The change-of-coefficients maps are compatible with composition: for $M\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)$ and
$K\in D^b_{\mathrm{ctf}}(Z_{\mathrm{pro}\acute{e}t},A)$,

$$
b^{g\circ f}(M)=Rg_{!,B}(b^f(M))\circ b^g(Rf_{!,A}M),
\qquad
c^{g\circ f}(K)=f_B^!c^g(K)\circ c^f(g_A^!K).
$$

The first identity holds on each free term of a resolution of $B$ over $A$,
since the composition isomorphism is natural, and the totalization in
Lemma [lemma-sp-reduction] extends it to arbitrary $A\to B$. We get the
second by transposing under the composite adjunction.

On towers, the composition isomorphism for $Rf_{!,\bullet}$ is built from
the same constructions. The isomorphism
$(g\circ f)^!_\bullet\simeq f^!_\bullet g^!_\bullet$ is the isomorphism of
right adjoints given by the composite adjunction on towers. Since evaluation at
level $n$ carries the counits on towers to the finite counits
(Proposition [proposition-sp-tower-geometric]), the level $n$ of
these isomorphisms is the finite one, and by the identities above they commute
with the transition maps, which are built from $b$ and $c$. Applying
$R\varprojlim$ gives the integral composition isomorphisms

$$
R(g\circ f)_{!,\mathcal O_E}\simeq Rg_{!,\mathcal O_E}Rf_{!,\mathcal O_E},
\qquad
(g\circ f)_{\mathcal O_E}^{!}\simeq f_{\mathcal O_E}^{!}g_{\mathcal O_E}^{!},
$$

between $\Dbc(X,\mathcal O_E)$ and $\Dbc(Z,\mathcal O_E)$; for $E=\mathbf Q_\ell$ the
coefficients are $\mathbf Z_\ell$. As for base change, inverting $\ell$ and extending
scalars give the composition isomorphisms with coefficients $E$ and $\overline{\mathbf Q}_\ell$.
These isomorphisms $(g\circ f)^!\simeq f^!g^!$ are the composition isomorphisms of
Proposition [proposition-composition-open-restriction-compactifications-f](1).
Indeed, the isomorphism of that proposition is characterized by the following
property: it carries the counit of $R(g\circ f)_!\dashv(g\circ f)^!$,
composed with the composition isomorphism for $Rf_!$, to the composite of
the counits for $f$ and $g$. By uniqueness of adjoints it therefore
suffices to check this property for every coefficient ring. With finite
coefficients it holds by definition. On towers the composition isomorphism
is the one of the composite adjunction, so in $D(\operatorname{Tow})$ it
carries the counit on towers of $g\circ f$ to the composite of the counits
on towers. By the comparison following the construction of $e_{f,\bullet}$
in Subsection [subsec-Base-change-and-composition], $\operatorname{red}$ carries the counits
and the composition isomorphism for $Rf_!$ with coefficients $\mathcal O_E$
to those on towers, and applying $R\varprojlim$ gives the property over
$\mathcal O_E$. Similarly, the same comparison shows that extension of scalars along
$\mathcal O_E\to E$ and $E\to\overline{\mathbf Q}_\ell$ carries the counits and the
composition isomorphisms for $Rf_!$ to the corresponding ones, which gives
the property over $E$ and $\overline{\mathbf Q}_\ell$.

With these composition isomorphisms in place for every coefficient ring,
the statement takes the following form. In topological terms it says that
the orientation of a composite of submersions is the product of the
orientations.
