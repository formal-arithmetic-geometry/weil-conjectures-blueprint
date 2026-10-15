+++
kind = "proof"
of = "det-ind-heart-extensions"
+++
Write $N=\varinjlim_\beta D_\beta$ and $B=\varinjlim_\alpha C_\alpha$ as filtered colimits of
constructible sheaves.

*Pullback to $C_\alpha$.* Let $M_\alpha=M\times_BC_\alpha$; it is an extension
$0\to N\to M_\alpha\to C_\alpha\to0$, with class $e_\alpha\in\Ext^1_\Lambda(C_\alpha,N)$. By
[sk-lem-constructible-ext-continuity] (degree $1$, targets in degree $0$),

$$
\Ext^1_\Lambda(C_\alpha,N)=\varinjlim_\beta\Ext^1_\Lambda(C_\alpha,D_\beta),
$$

so $e_\alpha$ is the pushout along $D_\beta\to N$ of an extension
$0\to D_\beta\to M_{\alpha\beta}\to C_\alpha\to0$ for some $\beta$. For $\beta'\geq\beta$ let
$M_{\alpha\beta'}$ be its pushout along $D_\beta\to D_{\beta'}$. Each $M_{\alpha\beta'}$ is an extension
of constructible sheaves, hence constructible (part (1) of [sk-lem-coefficient-heart]).

*Colimit over $\beta'$.* Pushouts commute with colimits, so
$\varinjlim_{\beta'}M_{\alpha\beta'}$ is the pushout of $M_{\alpha\beta}$ along $D_\beta\to N$, which
represents $e_\alpha$, i.e. is isomorphic to $M_\alpha$ as an extension. Thus
$M_\alpha\in\IndCons(X,\Lambda)$.

*Colimit over $\alpha$.* Filtered colimits are exact, so
$\varinjlim_\alpha M_\alpha=M\times_B\varinjlim_\alpha C_\alpha=M\times_BB=M$. By
[det-ind-heart-filtered-colimits], $M\in\IndCons(X,\Lambda)$.
