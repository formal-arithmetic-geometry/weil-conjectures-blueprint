+++
kind  = "proof"
of    = "lem-zl-morphism-open-closed-reduction"
+++
*Step 0: exact sequences of sheaves.* Let $A\xrightarrow{a}B
\xrightarrow{b}C$ be an exact sequence of constructible Weil sheaves on
$Y_0$ with $A$ and $C$ $\iota$-mixed of weights at most $u$. Then $B$ is
$\iota$-mixed of weights at most $u$. Indeed, put
$B'=\operatorname{im}(a)$, a Weil quotient of $A$, and note that $B/B'$
is a Weil subsheaf of $C$ by exactness. Both are $\iota$-mixed of
weights at most $u$ by [lem-a1-mixed-direct-summand](1), and then so is
the extension $0\to B'\to B\to B/B'\to0$ by
[lem-a1-mixed-direct-summand](2).

*Restriction.* If $h:W_0\hookrightarrow X_0$ is a locally closed
immersion and $\mathcal F$ is mixed of weights at most $w$, then so is
$h^*\mathcal F$: restrict the filtration; a closed point of $W_0$ is a
closed point of $X_0$ with the same residue field, stalk and local
Frobenius. Applied to cohomology sheaves, $h^*$ carries
$D_{\le w}(X_0)$ into $D_{\le w}(W_0)$.

*Part 1.* For a Weil complex $K$ on $X_0$ take the open–closed
recollement triangle $j_{0!}j_0^*K\to K\to i_{0*}i_0^*K\to$ of
[def-weil-open-closed-recollement], which exists and is
Weil-equivariant by [prop-sf-open-closed-triangle-all-stages]. Applying
$Rf_{0!}$ and the composition constraint of item (3) of
[prop-functor-package] (with its Weil descent, item (1)) gives the
distinguished triangle

$$
R(f_0j_0)_!\,j_0^*K\longrightarrow Rf_{0!}K\longrightarrow
R(f_0i_0)_!\,i_0^*K\longrightarrow .
$$

Complex form: if $K\in D_{\le w}(X_0)$, then $j_0^*K$ and $i_0^*K$ lie
in $D_{\le w}$ by the restriction remark, so the outer terms lie in
$D_{\le w}(Y_0)$ by hypothesis, and
[lem-zl-complex-extension] gives $Rf_{0!}K\in D_{\le w}(Y_0)$.
Sheaf form: take $K=\mathcal F$ in degree zero. The long exact
sequence of cohomology sheaves ([lem-sp-long-exact-of-triangle])
contains the exact sequence

$$
R^r(f_0j_0)_!\,j_0^*\mathcal F\longrightarrow R^rf_{0!}\mathcal F
\longrightarrow R^r(f_0i_0)_!\,i_0^*\mathcal F
$$

of Weil sheaves. The restrictions $j_0^*\mathcal F$, $i_0^*\mathcal F$
are mixed of weights at most $w$, so the outer terms are mixed of
weights at most $w+r$ by hypothesis, and Step 0 gives the claim for the
middle term.

*Part 2.* By arbitrary base change for compact-support direct images,
item (4) of [prop-functor-package], applied to the Cartesian squares
over $j'_0$ and $i'_0$,

$$
j_0'^{*}Rf_{0!}K\simeq Rf_{V!}\bigl(K|_{f_0^{-1}V_0}\bigr),
\qquad
i_0'^{*}Rf_{0!}K\simeq Rf_{T!}\bigl(K|_{f_0^{-1}T_0}\bigr),
$$

Weil-equivariantly. Complex form: for $K\in D_{\le w}(X_0)$ the
restrictions of $K$ lie in $D_{\le w}$, so the right sides lie in
$D_{\le w}(V_0)$ and $D_{\le w}(T_0)$. Extension by zero $j'_{0!}$ has
the same stalks at points of $V_0$ and zero stalks elsewhere, and
extends filtrations by zero, so
$j'_{0!}j_0'^{*}Rf_{0!}K\in D_{\le w}(Y_0)$; the finite pushforward
bound [lem-zl-finite-pushforward] gives
$i'_{0*}i_0'^{*}Rf_{0!}K\in D_{\le w}(Y_0)$. The target devissage
[lem-zl-open-closed-weight] then gives $Rf_{0!}K\in D_{\le w}(Y_0)$.
Sheaf form: the pullbacks $j_0'^*$, $i_0'^*$ are exact, so taking
$\mathcal H^r$ in the displayed isomorphisms for $K=\mathcal F$ shows
that $G=R^rf_{0!}\mathcal F$ has $j_0'^*G$ and $i_0'^*G$ mixed of weights
at most $w+r$. Applying the same argument to $G$ in degree zero gives
$G[0]\in D_{\le w+r}(Y_0)$, i.e. $G$ is mixed of weights at most $w+r$.
The stratified version follows by induction on the number of
open–closed steps.

*Part 3.* The short exact sequence is a distinguished triangle ([lem-weil-heart-short-exact-triangles])
$\mathcal F'\to\mathcal F\to\mathcal F''\to$; applying the exact functor
$Rf_{0!}$ and taking cohomology sheaves
([lem-sp-long-exact-of-triangle]) gives exact sequences
$R^rf_{0!}\mathcal F'\to R^rf_{0!}\mathcal F\to R^rf_{0!}\mathcal F''$,
and Step 0 applies. For a finite filtration, induct on its length using
the sequences $0\to\mathcal F_{i-1}\to\mathcal F_i\to
\mathcal F_i/\mathcal F_{i-1}\to0$.
