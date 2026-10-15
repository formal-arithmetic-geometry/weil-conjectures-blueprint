+++
kind = "proof"
of = "det-ind-heart-kernels-cokernels"
+++
*Filtered.* A finite diagram in $P_f$ is a finite diagram of arrows $v_k\colon C_k\to D_k$ with
compatible maps to $f$. Its colimit in the arrow category of $\Cons(X,\Lambda)$ is computed by finite
colimits of the $C_k$ and of the $D_k$, which exist since $\Cons(X,\Lambda)$ is abelian (part (1) of
[sk-lem-coefficient-heart]); the maps to $B$, $B'$ factor through these colimits by their universal
property. So every finite diagram has a cocone, and $P_f$ is filtered.

*Cofinality of $P_f\to J(B)$.* (i) Every $(C,c)\in J(B)$ is in the image up to a map: the composite
$f\circ c\colon C\to B'$ factors through some $(D,d)\in J(B')$ by finite presentation
([det-ind-heart-full-faithfulness], [det-ind-heart-canonical-presentation]), giving a square
$(C\to D)$. (ii) Two lifts $(C\xrightarrow{v_1}D_1)$, $(C\xrightarrow{v_2}D_2)$ of $(C,c)$ are dominated
by $(C\to D_1\oplus D_2)$. (iii) If a map $C_0\to C$ in $J(B)$ and lifts over $C_0$ and $C$ are given,
the two composites $C_0\to D$ agree after mapping to $B'$; by finite presentation of $C_0$ they agree
after composing with some $D\to D'$ in $J(B')$, which can be chosen as the cokernel of their
difference. Explicitly: two choices over $C_0$ are dominated by the square with source
$C_1\amalg_{C_0}C_2$ and target the quotient of $D_1\oplus D_2$ by the two images of $C_0$, and
parallel choices are dominated by their cokernel. These are the cofinality conditions.

*Cofinality of $P_f\to J(B')$.* Every $(D,d)$ is the target of the square $(0\to D)$; the domination
arguments are the same.

*Colimits.* By cofinality and [det-ind-heart-canonical-presentation],
$\varinjlim_{P_f}C=\varinjlim_{J(B)}C=B$ and $\varinjlim_{P_f}D=B'$, compatibly with $v$ and $f$, so
$f=\varinjlim_{P_f}v$. Filtered colimits are exact in $\Mod(X_{\mathrm{proét}},\Lambda)$, hence commute with
kernels and cokernels. Each $\ker v$, $\coker v$ is constructible, so their filtered colimits lie in
$\IndCons(X,\Lambda)$.
