+++
id = "rem-dl-a1-conventions"
kind = "definition"
title = "Affine-line and weight conventions"
order = 3975
uses = ["def-weil-frobenius-detailed", "def-weil-punctual-weights", "def-wf-middle-extension", "def-wf-tate-twist", "sk-lem-coefficient-heart", "sk-def-sf-weil-complexes"]
lean = ["AlgebraicGeometry.WeilSheaf.IsGeometricallyConstant", "AlgebraicGeometry.WeilSheaf.IsUnramifiedAtInfinity", "AlgebraicGeometry.WeilSheaf.IsIrreducibleLisse"]
+++
Fix $k_0=\mathbf F_q$, its algebraic closure $k$, a prime $\ell\ne \operatorname{char}(k_0)$, and a field embedding $\iota:\DLAQ\hookrightarrow\mathbf C$. Write
$A_0=\mathbf A^1_{k_0}$, $A=A_0\otimes k$, and use a prime to denote the
dual affine line. All cohomology is geometric, with geometric Frobenius
([def-weil-frobenius-detailed]).
A *Weil sheaf* on a $k_0$-scheme $U_0$, with $U=U_0\otimes k$, is a constructible
$\overline{\mathbf Q}_{\ell,U}$-module $F$ on $U_{\mathrm{proét}}$ with a Weil structure $\operatorname{Fr}_U^*F\xrightarrow{\sim}F$ ([sk-lem-coefficient-heart], [sk-def-sf-weil-complexes]); it is *lisse* if $F$ is locally free of finite rank for the pro-étale topology.
A lisse Weil sheaf is *pure of weight $w$* if every eigenvalue
$\alpha$ at a closed point $x$ satisfies
$|\iota\alpha|=q_x^{w/2}$; replace equality by $\leq$ for an upper bound
([def-weil-punctual-weights]).
The twist $(-1)$ raises weights by two ([def-wf-tate-twist]).
A Weil sheaf $F$ is *irreducible lisse* (an *irreducible lisse Weil
sheaf*) if it is lisse and nonzero and every lisse Weil subsheaf of $F$
is $0$ or $F$: it is a simple object of the category of lisse Weil
sheaves. On a connected normal scheme such as a dense open of $A_0$, this
says that the Weil group acts irreducibly on the geometric generic stalk.
It is weaker than simplicity in the category of all Weil sheaves, which
never holds for a nonzero lisse sheaf on a curve: for a closed point $x$,
the extension by zero of the restriction to the complement of $x$ is a
nonzero proper subsheaf.

For a dense open $j:U_0\hookrightarrow A_0$, $j_*F$ denotes the
*ordinary* sheaf direct image. Its stalks at missing points are
inertia invariants; its curve perverse intermediate extension is
$j_{!*}(F[1])=(j_*F)[1]$ ([def-wf-middle-extension]). A lisse Weil sheaf $F$ on $U_0$ is *unramified at infinity* if it
extends to a lisse Weil sheaf on the open $U_0\cup\{\infty\}$ of
$\mathbf P^1_{k_0}$ (with $A_0\subset\mathbf P^1_{k_0}$ the standard chart);
equivalently, inertia
at $\infty\in\mathbf P^1_k$ acts trivially on the geometric generic fiber.
A Weil sheaf on $U_0$ is *geometrically constant* if its underlying
$\overline{\mathbf Q}_{\ell,U}$-module on $U_{\mathrm{proét}}$ ([sk-lem-coefficient-heart]) is
constant on every connected open $V$ of $U=U_0\otimes k$, that is, isomorphic there to
$\overline{\mathbf Q}_{\ell,V}\otimes_{\Qlb}W=p_V^*\underline W$ for a finite-dimensional
$\Qlb$-vector space $W$; for $U$ connected this means that the geometric fundamental group
acts trivially, while its Frobenius module may be nontrivial.
