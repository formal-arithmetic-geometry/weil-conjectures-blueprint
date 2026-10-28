+++
id = "prose-10-23"
kind = "hidden"
title = "Composition isomorphisms for all coefficients"
order = 3371
+++
**Composition.**
The same pattern applies to composition: we fix the composition
isomorphisms for $f^!$ with every coefficient ring, and then compare the maps
$\gamma$. From now on, $g$ no longer denotes the base change in a square: let
$X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions
$d$ and $e$. Composing the finite adjunctions, we identify
$(g\circ f)_A^!$ with $f_A^!g_A^!$, compatibly with
$R(g\circ f)_{!,A}\simeq Rg_{!,A}Rf_{!,A}$, and the counit of the
composite adjunction is the composite of the two counits.

The change-of-coefficients maps are compatible with composition: for $M\in\Dctf(X_{\mathrm{pro\acute et}},A)$ and
$K\in\Dctf(Z_{\mathrm{pro\acute et}},A)$,

$$
b^{g\circ f}(M)=Rg_{!,B}(b^f(M))\circ b^g(Rf_{!,A}M),
 \qquad
 c^{g\circ f}(K)=f_B^!c^g(K)\circ c^f(g_A^!K).
$$

The first identity holds on each free term of a resolution of $B$ over $A$,
since the composition isomorphism is natural, and the totalization in
Lemma [sk-lem-sp-reduction] extends it to arbitrary $A\to B$. We get the
second by transposing under the composite adjunction. At each level, the
composition isomorphisms for towers are the finite ones, and by these
identities they commute with the transition maps, which are built from
$b$ and $c$. Hence they are isomorphisms of functors on towers. Applying
$R\varprojlim$, we obtain the integral composition isomorphisms

$$
R(g\circ f)_{!,\mathcal O_E}\simeq Rg_{!,\mathcal O_E}Rf_{!,\mathcal O_E},
 \qquad
 (g\circ f)_{\mathcal O_E}^{!}\simeq f_{\mathcal O_E}^{!}g_{\mathcal O_E}^{!},
$$

between $\Dbc(X,\mathcal O_E)$ and $\Dbc(Z,\mathcal O_E)$; for $E=\Ql$ the
coefficients are $\Zl$. As for base change, inverting $\ell$ and extending
scalars give the composition isomorphisms with coefficients $E$ and $\overline{\mathbf Q}_\ell$.
