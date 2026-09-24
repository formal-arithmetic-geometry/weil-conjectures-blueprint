+++
id = "lemma-weil-pbc-completed-map-reduction"
kind = "lemma"
title = "Finite reduction of the completed map"
order = 2002
uses = ["def-weil-pbc-completed-frobenius-structures", "def-weil-pbc-completed-reduction-square", "lemma-weil-pbc-completed-frobenius-equivariance", "lemma-weil-pbc-frobenius-tower-compatibility", "lemma-weil-pbc-level-map-derived-limit"]
+++
For every $n$, the diagram

$$
\begin{CD}
S\otimes^LP_n @>{\overline\xi_n}>> T\otimes^LP_n\\
@V{\alpha_n}V{\sim}V @VV{\delta_n}V{\sim}\\
B_n @>{v'_n}>> D_n
\end{CD}
$$

commutes. Hence reduction of
$\operatorname{Ex}^{\mathrm{comp}}_{\square,K}$ modulo $I^n$, conjugated
by the displayed canonical reduction isomorphisms, is exactly the S8
transported finite-level exchange map $v'_n=\operatorname{Ex}_{\square,K_n}$.
The squares for $n+1\to n$ commute, and the assertion is natural for
compatible tower endomorphisms. Under a Frobenius-equivariant datum, use
$\Phi_{Y'}P_n=P_n$ to give the two reductions their induced Weil structures.
Then

$$
\begin{aligned}
\alpha_n(\Theta_S\otimes1)
&=\Theta_{B,n}\Phi_{Y'}(\alpha_n),\\
\delta_n(\Theta_T\otimes1)
&=\Theta_{D,n}\Phi_{Y'}(\delta_n),
\end{aligned}
$$

and the displayed reduction square is a square of Weil objects.

## Proof

Under $S=A_\infty$ and the direct-image completion identification
$T\simeq C_\infty$, the completed exchange map is both limit composites

$$
V'H=H'V:A_\infty\longrightarrow D_\infty,
$$

followed by the inverse of direct-image/limit commutation. More explicitly,
if $d:T\to D_\infty$ is direct-image/limit commutation and
$c:C_\infty\to T$ is direct-image completion, then its construction gives
$dc=H'$. Functorial finite
reduction and the component equations of the limit rectangle give

$$
\tau_n\overline\xi_n=v_n\sigma_n.
$$

Consequently the two composites around the completed reduction square are

$$
\delta_n\overline\xi_n
=h'_n\tau_n\overline\xi_n=h'_nv_n\sigma_n
$$

and

$$
v'_n\alpha_n=v'_nh_n\sigma_n.
$$

They are equal term by term because $h'_nv_n=v'_nh_n$ in the finite-level
rectangle. Naturality of finite reduction makes $\sigma_n$ and $\tau_n$
commute with $n+1\to n$, and functoriality of tensor reduction does the same
for $\overline\xi_n$. Together with the four transition equations, this
shows that the completed squares commute with $K_{n+1}\to K_n$ on every
corner. The limit construction and all four reduction edges are
operator-equivariant, so the conjugated equality is operator-natural as well.

For Frobenius, the definition of $\Theta_S$ transports
$\Theta_{A,\infty}$ across $s$, and the $n$th product-cone component followed
by $h_n$ is $\alpha_n$. This gives the first displayed Weil equation. The
definition of $\Theta_T$ transports $\Theta_{D,\infty}$ across $t$, and its
$n$th component is $\delta_n$, giving the second. The completed Frobenius
equation for $\overline\xi_n$, together with finite-level equivariance of
$v'_n$, now says that every arrow of the reduction square is a Weil morphism.
