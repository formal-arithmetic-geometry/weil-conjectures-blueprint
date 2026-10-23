+++
kind = "proof"
of = "lem-factors-through-localization-of-smooth"
+++
Choose a finite presentation $C=R[x_1,\dots,x_n]/(r_1,\dots,r_m)$. Clear the finitely many denominators of the images $g(x_i)$ with a product $s_0\in S$, so that $g(x_i)=a_i/s_0$ with $a_i\in P$, and let $f_0:R[x_1,\dots,x_n]\to P_{s_0}$ send $x_i$ to $a_i/s_0$. Each relation $f_0(r_j)$ maps to zero in $S^{-1}P$; by the equality criterion in a localization there is $t_j\in S$ killing a numerator of $f_0(r_j)$. Put $s=s_0\prod_jt_j$. In $P_s$ all the $a_i/s_0$ are defined and all relations vanish, giving $f:C\to P_s$. The universal property of $P_s$ gives $h:P_s\to S^{-1}P$, since $s$ is invertible in $S^{-1}P$, and $h\circ f=g$ holds on the generators $x_i$, hence everywhere. Empty products are $1$, and $0\in S$ is allowed.
