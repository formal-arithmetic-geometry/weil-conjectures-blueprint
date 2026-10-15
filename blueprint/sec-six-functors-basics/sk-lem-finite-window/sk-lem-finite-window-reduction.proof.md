+++
kind = "proof"
of = "det-finite-window-reduction"
+++
*Upper truncation.* From the triangle $\tau_{\leq0}K\to K\to\tau_{>0}K\to$ we get the exact sequence

$$
\Hom(C,\tau_{>0}K[-1])\to\Hom(C,\tau_{\leq0}K)\to\Hom(C,K)\to\Hom(C,\tau_{>0}K).
$$

Since $C$ is a sheaf in degree $0$ and $\tau_{>0}K[s]\in\D^{\geq1}$ for $s=0,-1$, the outer terms vanish
($t$-structure axiom: no maps from $\D^{\leq0}$ to $\D^{\geq1}$).

*Lower truncation.* Put $K'=\tau_{\leq0}K$ and $L=\tau_{\leq-d_C-1}K'$. The triangle
$L\to K'\to\tau_{\geq-d_C}K'\to L[1]$ gives

$$
\Hom(C,L)\to\Hom(C,K')\to\Hom(C,\tau_{\geq-d_C}K')\to\Hom(C,L[1]).
$$

Both $L$ and $L[1]$ lie in $\Dic(X,\Lambda)$ ([sk-cor-ambient-ind-derived]) and have cohomology in degrees
$\leq-d_C-1$ (resp. $\leq-d_C-2$), so the outer terms vanish by hypothesis (which holds by
[det-finite-window-unbounded]). Hence the middle map is an isomorphism; note
$\tau_{\geq-d_C}K'=\tau_{\geq-d_C}\tau_{\leq0}K$.

*Shift.* For general $m$, apply this to $K[m]$, using $\tau_{\leq0}(K[m])=(\tau_{\leq m}K)[m]$ and
$\tau_{\geq-d_C}(K[m])=(\tau_{\geq m-d_C}K)[m]$. Naturality in $K$ is clear since all maps are truncation
maps.
