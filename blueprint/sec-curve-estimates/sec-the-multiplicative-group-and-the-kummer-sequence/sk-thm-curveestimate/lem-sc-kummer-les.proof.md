+++
kind  = "proof"
of    = "lem-sc-kummer-les"
+++
Take the long exact sequence in cohomology of the exact
[def-sc-kummer-sequence] ([lem-sc-kummer-exact]):

$$
\begin{array}{l}
0\to H^0(C,\mu_n)\to H^0(C,\mathbf G_m)\xrightarrow{n}
H^0(C,\mathbf G_m)\to
H^1(C,\mu_n)\to H^1(C,\mathbf G_m)\xrightarrow{n}\\
\hphantom{0\to{}}
H^1(C,\mathbf G_m)\to H^2(C,\mu_n)\to H^2(C,\mathbf G_m)\to\cdots.
\end{array}
$$

Here $H^0(C,\mathbf G_m)=\mathcal O_C(C)^\times$ and $k$ is
algebraically closed, so $x\mapsto x^n$ is surjective on the
constant part $k^\times\subseteq\mathcal O_C(C)^\times$;
$H^1(C,\mathbf G_m)=\operatorname{Pic}(C)$ by
[lem-sc-h1-gm-pic]; and the term $H^2(C,\mathbf G_m)$ is zero
by assumption. Exactness of the sequence at
$H^1(C,\mu_n)$ and at $H^1(C,\mathbf G_m)$ therefore gives the
displayed short exact sequence and the displayed formula for
$H^2(C,\mu_n)$; for connected $C$ the $H^0$-term is
$\mu_n(k)=\mathbf Z/n\mathbf Z$ by
[lem-sc-primitive-root]. The last assertion follows because for
$C$ proper, connected and reduced the only units are the constants
$k^\times$, which are $n$-divisible since $k$ is algebraically
closed.
