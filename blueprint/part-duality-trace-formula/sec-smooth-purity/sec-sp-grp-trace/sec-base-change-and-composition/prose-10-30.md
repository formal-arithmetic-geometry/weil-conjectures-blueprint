+++
id = "prose-10-30"
kind = "hidden"
title = "Base change and composition"
order = 484
+++
The trace map is built from the map $\gamma_f$ of (10.1). Its transitivity, and its
compatibility with Frobenius in Section [sec-frobenius], therefore depend on
the compatibility of $\gamma_f$ with base change and with composition. At finite level both compatibilities
follow from the construction of Section [sec-sp-grp-finite]. To pass to
$\Zl$ we use towers, and for this the isomorphisms at finite level have to
commute with change of finite coefficients.

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
Definition [sk-def-sp-scalar-extension].

**Change of coefficients and towers.**
The statement of Proposition [sk-prop-sp-purity-bc] needs an exceptional
base change isomorphism for $\Zl$, which we obtain as a limit of the
finite ones. For this limit to exist, the finite isomorphisms must commute
with the reduction maps, and this is what we check first.
For $M\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)$ and $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$, let
$b^f(M):(Rf_{!,A}M)_B\xrightarrow{\sim}Rf_{!,B}M_B$ and
$c^f(K):(f_A^!K)_B\xrightarrow{\sim}f_B^!K_B$ be the change-of-coefficients
maps of Lemma [sk-lem-sp-reduction]. With
$g'^*:D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)\to D^b_{\mathrm{ctf}}(X'_{\mathrm{pro}\acute{e}t},A)$ and
$g^*:D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)\to D^b_{\mathrm{ctf}}(Y'_{\mathrm{pro}\acute{e}t},A)$, let
$\beta_{f,A}(M):g^*Rf_{!,A}M\xrightarrow{\sim}Rf'_{!,A}g'^*M$ be
the base change map for compact support, and let
$e_{f,A}(K):g'^*f_A^!K\xrightarrow{\sim}f'^!_Av^*K$ be the
exceptional base change isomorphism of
Proposition [sk-prop-cohsm](3). We claim that base change commutes with
change of coefficients, i.e.,

$$
\beta_{f,B}(M_B)\circ g^*(b^f(M))
=b^{f'}(g'^*M)\circ\bigl(\beta_{f,A}(M)\bigr)_B,
\tag{10.21}
$$

$$
c^{f'}(g^*K)\circ(e_{f,A}(K))_B
=e_{f,B}(K_B)\circ g'^*c^f(K).
\tag{10.22}
$$

To prove (10.21), choose a compactification
$f=\bar f\circ j$ and pull it back to $Y'$. Since $b$ and $\beta$ for $f$
are the composites of those for $j$ and for $\bar f$, it suffices to treat
these two cases. For the open immersion $j$,
extension by zero commutes with pullback and with extension of scalars,
and both sides of (10.21) are this identification. For the
proper map $\bar f$, both $b^{\bar f}$ and proper base change are
transposes of the counit of $L\bar f^*\dashv R\bar f_*$ on the derived
categories of sheaves of $A$-modules on the pro-étale sites, after extension
of scalars and after pullback respectively. Therefore both sides of
(10.21) transpose to the pulled-back counit with
scalars extended. The second identity reduces to the first. Recall that
$c^f$ and $e_{f,A}$ are defined by transposing
the counit composed with $(b^f)^{-1}$, respectively with $\beta_{f,A}^{-1}$
(see (10.15)). Transposing both sides of
(10.22) under
$Rf'_{!,B}\dashv f'^!_B$, we therefore get two maps
$Rf'_{!,B}\bigl(g'^*((f_A^!K)_B)\bigr)\to g^*K_B$, each built from the
counit $\varepsilon_{f,A}(K)$, the comparisons $b$ and the base change
maps $\beta$. By naturality of $b$ and $\beta$, and since the counit
commutes with extension of scalars and with pullback, the two maps agree
once (10.21) holds.

Now let $E/\Ql$ be a finite extension and work in the category of
towers of (10.17). Extension by zero and proper
base change define $\beta_{f,\bullet}:g^*Rf_{!,\bullet}\to Rf'_{!,\bullet}g'^*$,
and transposing $g^*(\varepsilon_{f,\bullet})\circ\beta_{f,\bullet}^{-1}$
under the adjunction on towers for $f'$ defines
$e_{f,\bullet}:g'^*f_\bullet^!\to f'^!_\bullet g^*$. At
level $n$ these are $\beta_{f,\mathcal O_E/\ell^n}$ and the exceptional
base change map with coefficients $\mathcal O_E/\ell^n$, so they are
isomorphisms; for the second, this is
Proposition [sk-prop-cohsm](3) with
$\Lambda=\mathcal O_E/\ell^n$. The transition maps of $f_\bullet^!$ are
induced by the change-of-coefficients maps $c$
(Proposition [sk-prop-sp-tower-geometric]), so
(10.22) says that the levels of $e_{f,\bullet}$
commute with them. Hence $e_{f,\bullet}$ is an isomorphism of functors on
towers, and for a normalized tower $K_\bullet$ both
$g'^*f_\bullet^!K_\bullet$ and $f'^!_\bullet g^*K_\bullet$
are normalized.

Let $K\in\Dbc(Y,\mathcal O_E)$, and let
$\operatorname{red}_YK=(K/\ell^n)_n$ be its tower of reductions
(Lemma [sk-lem-sp-tower]). Inverse image commutes
with reduction modulo $\ell^n$, and
$f_{\mathcal O_E}^!K\simeq R\varprojlim_nf_{\mathcal O_E/\ell^n}^!(K/\ell^n)$
by Proposition [sk-prop-sp-integral-adjunction] and
(10.19). Hence both sides below are $R\varprojlim_n$
of the corresponding terms at level $n$ for $K/\ell^n$, and applying
$R\varprojlim$ to $e_{f,\bullet}$ at $\operatorname{red}_YK$ we obtain the
integral exceptional base change isomorphism

$$
g'^{*}f_{\mathcal O_E}^{!}K
\xrightarrow{\sim}f'^{!}_{\mathcal O_E}g^{*}K;
\tag{10.23}
$$

for $E=\Ql$ the coefficients are $\Zl$. With coefficients $E$ and $\overline{\mathbf Q}_\ell$
we define exceptional base change by inverting $\ell$ in
(10.23) on integral models and then extending scalars
from a finite extension of $\Ql$; this is possible because $f^*$, $f^!$
and $Rf_!$ with these coefficients are obtained from the integral functors
in the same way (Proposition [sk-prop-sp-rational] and
Theorem [sk-thm-sp-qbar]).
