+++
id = "prose-09-30"
kind = "hidden"
title = "Base change and composition (1)"
order = 797
+++
Fix a cartesian square

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y,
\end{CD}
$$

with $f$ smooth of pure relative dimension $d$, and a map $A\to B$ of
finite commutative rings killed by a power of $\ell$. A subscript $B$
denotes extension of scalars, as in
Definition [definition-sp-scalar-extension].

**Base change.** The statement of
Proposition [proposition-compatibility-purity-base-change] needs an
[exceptional base change isomorphism](@definition-exceptional-base-change-map) for $\mathbf Z_\ell$. It is obtained as a limit of
the finite ones, and the limit exists once the finite isomorphisms commute
with the reduction maps, that is, once base change commutes with change of
coefficients. To state this we name the four comparison maps
involved. For $M\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)$ and $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},A)$, let
$b^f(M):(\href{@proposition-construction-independence-rf-shriek}{Rf_{!,A}M})_B\xrightarrow{\sim}\href{@proposition-construction-independence-rf-shriek}{Rf_{!,B}}\href{@definition-sp-scalar-extension}{M_B}$ and
$c^f(K):(\href{@theorem-existence-exceptional-inverse-image}{f_A^!K})_B\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{f_B^!}\href{@definition-sp-scalar-extension}{K_B}$ be the change-of-coefficients
maps of Lemma [lemma-sp-reduction]. With
$g'^*:\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)\to \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{X'_{\mathrm{pro}\acute{e}t}},A)$ and
$g^*:\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},A)\to \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y'_{\mathrm{pro}\acute{e}t}},A)$, let
$\beta_{f,A}(M):g^*\href{@proposition-construction-independence-rf-shriek}{Rf_{!,A}M}\xrightarrow{\sim}\href{@proposition-construction-independence-rf-shriek}{Rf'_{!,A}g'^*M}$ be
the base change map for compact support, and let
$e_{f,A}(K):g'^*\href{@theorem-existence-exceptional-inverse-image}{f_A^!K}\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{f'^!_Ag^*K}$ be the
[exceptional base change isomorphism](@definition-exceptional-base-change-map) of
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3). The claim is

$$
\beta_{f,B}(\href{@definition-sp-scalar-extension}{M_B})\circ g^*(b^f(M))
=b^{f'}(g'^*M)\circ\bigl(\beta_{f,A}(M)\bigr)_B,
\tag{9.22}
$$

$$
c^{f'}(g^*K)\circ(e_{f,A}(K))_B
=e_{f,B}(\href{@definition-sp-scalar-extension}{K_B})\circ g'^*c^f(K).
\tag{9.23}
$$

Both identities say that two ways of passing from $(A,Y)$ to $(B,Y')$
give the same map: changing coefficients first and then base, or the other
way round. We prove the first by splitting [$Rf_!$](@proposition-construction-independence-rf-shriek) into an open and a proper
part, and deduce the second from the first by transposition.

To prove (9.22), choose a compactification
$f=\bar f\circ j$ and pull it back to $Y'$. Since $b$ and $\beta$ for $f$
are the composites of those for $j$ and for $\bar f$, it suffices to treat
these two cases. For the open immersion $j$, extension by zero commutes
with pullback and with [extension of scalars](@definition-sp-scalar-extension), and both sides of
(9.22) are this identification. For the proper map $\bar f$, both $b^{\bar f}$ and [proper base change](@theorem-proper-base-change-classical-pro) are
transposes of the counit of $L\bar f^*\dashv R\bar f_*$, the first after
[extension of scalars](@definition-sp-scalar-extension) and the second after pullback; here we work on the derived
categories of sheaves of $A$-modules on the [pro-étale sites](@definition-small-pro-etale-site). Therefore
both sides of (9.22) transpose to the
pulled-back counit with scalars extended.

For the second identity, recall that $c^f$ and $e_{f,A}$ are defined by
transposing the counit composed with $(b^f)^{-1}$, respectively with
$\beta_{f,A}^{-1}$ (see (9.16)). Transposing both
sides of (9.23) under
$\href{@proposition-construction-independence-rf-shriek}{Rf'_{!,B}}\dashv \href{@theorem-existence-exceptional-inverse-image}{f'^!_B}$ thus gives two maps
$\href{@proposition-construction-independence-rf-shriek}{Rf'_{!,B}}\bigl(g'^*((\href{@theorem-existence-exceptional-inverse-image}{f_A^!K})_B)\bigr)\to g^*\href{@definition-sp-scalar-extension}{K_B}$. Each is built from the
counit $\varepsilon_{f,A}(K)$, the comparisons $b$ and the base change
maps $\beta$, and the counit commutes with [extension of scalars](@definition-sp-scalar-extension) and with
pullback. By naturality of $b$ and $\beta$, the two maps therefore agree
once (9.22) holds.

These two identities let us assemble the finite base change maps into a
single map of towers. Its levels are linked by the change-of-coefficients
maps along $\mathcal O_E/\ell^{n+1}\to\mathcal O_E/\ell^n$.

Let $E/\mathbf Q_\ell$ be a finite extension and work in the category of
towers of (9.18). Extension by zero and proper
base change define $\beta_{f,\bullet}:g^*Rf_{!,\bullet}\to Rf'_{!,\bullet}g'^*$,
and transposing $g^*(\varepsilon_{f,\bullet})\circ\beta_{f,\bullet}^{-1}$
under the adjunction on towers for $f'$ defines
$e_{f,\bullet}:g'^*\href{@proposition-sp-tower-geometric}{f_\bullet^!}\to \href{@proposition-sp-tower-geometric}{f'^!_\bullet} g^*$. At
level $n$ these are $\beta_{f,\mathcal O_E/\ell^n}$ and the [exceptional
base change map](@definition-exceptional-base-change-map) with coefficients $\mathcal O_E/\ell^n$, so they are
isomorphisms; for the second, this is
Proposition [proposition-exceptional-inverse-image-smooth-morphism](3) with
$\Lambda=\mathcal O_E/\ell^n$. Moreover, the transition maps of [$f_\bullet^!$](@proposition-sp-tower-geometric) are
induced by the change-of-coefficients maps $c$
(Proposition [proposition-sp-tower-geometric]), and by
(9.23) the levels of $e_{f,\bullet}$
commute with them. So $e_{f,\bullet}$ is an isomorphism of functors on
towers. In particular, for a normalized tower $K_\bullet$ both
$g'^*\href{@proposition-sp-tower-geometric}{f_\bullet^!K_\bullet}$ and [$f'^!_\bullet g^*K_\bullet$](@proposition-sp-tower-geometric)
are normalized.

The functors $\operatorname{red}$ of Lemma [lemma-sp-tower-adjunction-foundation]
carry the maps over $\mathcal O_E$ (base change, composition, counits and
transposes) to the maps on towers. We check this in steps. First, the functor
[$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation) is a derived pullback of ringed topoi, so it
commutes with $g^*$ by associativity of derived pullbacks, and it commutes
with extension by zero because the right adjoints commute. Next, for proper
$\bar f$, the comparison
$\href{@lemma-sp-tower-adjunction-foundation}{\operatorname{red}_YR\bar f_*M}\to R\bar f_{*,\bullet}\operatorname{red}_XM$ is the
transpose of [$\operatorname{red}_X$](@lemma-sp-tower-adjunction-foundation) of the counit of $\bar f^*\dashv R\bar f_*$,
and its level $n$ is the change-of-coefficients map of
Lemma [lemma-change-coefficients-direct-image] for
$\mathcal O_E\to\mathcal O_E/\ell^n$. As evaluations detect isomorphisms,
the comparison is an isomorphism for $M\in\href{@definition-constructible-sheaves}{\Dbc(X,\mathcal O_E)}$. Composing
with the compatibility with $j_!$ we obtain the comparison
$\operatorname{red}_Y\href{@proposition-construction-independence-rf-shriek}{Rf_{!,\mathcal O_E}M}\simeq Rf_{!,\bullet}\operatorname{red}_XM$
for a compactification $f=\bar f\circ j$. The formal argument in the proof of
Proposition [proposition-six-operations-change-coefficients] shows that,
under these comparisons, [$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation) carries the unit and counit of
$\bar f^*\dashv R\bar f_*$ over $\mathcal O_E$ to the unit and counit on towers.
Since the base change and composition isomorphisms of
Proposition [proposition-composition-base-change-rf-shriek] are composites
of such units and counits and of the identifications of pullbacks and of
extensions by zero, [$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation) carries them, with coefficients
$\mathcal O_E$, to $\beta_{f,\bullet}$ and to the corresponding composition
isomorphisms on towers. For the counit, the adjunction of
Proposition [proposition-sp-integral-adjunction] is transported from the
adjunction on towers, so [$\operatorname{red}_Y$](@lemma-sp-tower-adjunction-foundation) carries
$\varepsilon_f(K)$ to $\varepsilon_{f,\bullet}(\href{@lemma-sp-tower-adjunction-foundation}{\operatorname{red}_YK})$, once the
sources are identified by this comparison and by the isomorphism
$\operatorname{red}_X\href{@theorem-existence-exceptional-inverse-image}{f^!_{\mathcal O_E}K}\simeq \href{@proposition-sp-tower-geometric}{f^!_\bullet}\operatorname{red}_YK$
of its proof. Since a transpose is determined by the counit, [$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation)
also carries transposes under $\href{@proposition-construction-independence-rf-shriek}{Rf_{!,\mathcal O_E}}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!_{\mathcal O_E}}$ to
transposes on towers. Finally, by
Lemma [lemma-sp-tower-adjunction-foundation], $\operatorname{red}$ is an
equivalence on [$\Dbc(-,\mathcal O_E)$](@definition-constructible-sheaves) whose inverse is $R\varprojlim$. A
morphism of [$\Dbc(-,\mathcal O_E)$](@definition-constructible-sheaves) is therefore $R\varprojlim$ of its image under
[$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation), up to the unit isomorphisms
$M\simeq R\varprojlim\href{@lemma-sp-tower-adjunction-foundation}{\operatorname{red}M}$.

Let $K\in\href{@definition-constructible-sheaves}{\Dbc(Y,\mathcal O_E)}$, and let
$\operatorname{red}_YK=(K/\ell^n)_n$ be its tower of reductions
(Lemma [lemma-sp-tower-adjunction-foundation]). Since inverse image commutes
with reduction modulo $\ell^n$, and
$\href{@theorem-existence-exceptional-inverse-image}{f_{\mathcal O_E}^!K}\simeq R\varprojlim_n\href{@theorem-existence-exceptional-inverse-image}{f_{\mathcal O_E/\ell^n}^!(K/\ell^n)}$
by Proposition [proposition-sp-integral-adjunction] and
(9.20), both sides below are $R\varprojlim_n$
of the corresponding terms at level $n$ for $K/\ell^n$. Applying
$R\varprojlim$ to $e_{f,\bullet}$ at [$\operatorname{red}_YK$](@lemma-sp-tower-adjunction-foundation) we obtain the
integral [exceptional base change isomorphism](@definition-exceptional-base-change-map)

$$
g'^{*}\href{@theorem-existence-exceptional-inverse-image}{f_{\mathcal O_E}^{!}K}
\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{f'^{!}_{\mathcal O_E}g^{*}K};
\tag{9.24}
$$

for $E=\mathbf Q_\ell$ the coefficients are $\mathbf Z_\ell$. With coefficients $E$ and $\overline{\mathbf Q}_\ell$
we define exceptional base change by inverting $\ell$ in
(9.24) on integral models and then extending
scalars from a finite extension of $\mathbf Q_\ell$. This is possible because $f^*$,
[$f^!$](@theorem-existence-exceptional-inverse-image) and [$Rf_!$](@proposition-construction-independence-rf-shriek) with these coefficients are obtained from the integral
functors in the same way (Proposition [proposition-sp-rational] and
Theorem [theorem-sp-qbar]).

In each case the map obtained is the exceptional base change map of
Definition [definition-exceptional-base-change-map]. For $\mathcal O_E$,
the map of the definition is the transpose under
$\href{@proposition-construction-independence-rf-shriek}{Rf'_{!,\mathcal O_E}}\dashv \href{@theorem-existence-exceptional-inverse-image}{f'^!_{\mathcal O_E}}$ of
$g^*(\varepsilon_f(K))\circ\beta^{-1}$. By the preceding paragraph,
[$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation) carries this composite to
$g^*(\varepsilon_{f,\bullet})\circ\beta_{f,\bullet}^{-1}$ at
[$\operatorname{red}_YK$](@lemma-sp-tower-adjunction-foundation), and it carries the transpose to the transpose on
towers, which is $e_{f,\bullet}(\href{@lemma-sp-tower-adjunction-foundation}{\operatorname{red}_YK})$. Hence the map of
the definition is $R\varprojlim$ of $e_{f,\bullet}(\href{@lemma-sp-tower-adjunction-foundation}{\operatorname{red}_YK})$,
that is, (9.24). For $E$ and $\overline{\mathbf Q}_\ell$ we argue in
the same way, with extension of scalars along $\mathcal O_E\to E$ and
$E\to\overline{\mathbf Q}_\ell$ in place of [$\operatorname{red}$](@lemma-sp-tower-adjunction-foundation). Indeed, extension of scalars commutes
with $g^*$, extension by zero and $R\bar f_*$ through the
change-of-coefficients maps of
Definition [definition-change-of-coefficients-maps], and by
Proposition [proposition-six-operations-change-coefficients] it carries the
units and counits of $\bar f^*\dashv R\bar f_*$ and of $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ to
the corresponding units and counits. So it carries the base change maps for
[$Rf_!$](@proposition-construction-independence-rf-shriek), the counits, and therefore the [exceptional base change maps](@definition-exceptional-base-change-map) over
$\mathcal O_E$ to those over $E$. In the same way those over a finite
extension of $\mathbf Q_\ell$ go to those over $\overline{\mathbf Q}_\ell$.

Since the [exceptional base change map](@definition-exceptional-base-change-map) is an isomorphism for every
admissible coefficient ring, we can state that [$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients) commutes with it.
For $g$ the inclusion of a closed point $y$ of $Y$, this says that
[$\gamma_f$](@theorem-smooth-purity-all-admissible-coefficients) restricts on the fibre $X_y$ to the isomorphism [$\gamma$](@theorem-smooth-purity-all-admissible-coefficients) of the
smooth $\kappa(y)$-scheme $X_y$.
