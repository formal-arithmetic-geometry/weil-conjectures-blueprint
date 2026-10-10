+++
kind  = "proof"
of    = "lemma-nagata-conrad-strict-transform-in-charts"
+++
Both assertions are local on $X$, so let $X=\operatorname{Spec}(A)$ and put
$I=\Gamma(X,\mathcal I_Y)$ and $J=\Gamma(X,\mathcal I_{Y'})$. The charts
$U(s)$ for $s\in I\cup J$ cover $\widetilde X$ by
[prop-nagata-affine-blowup-chart-cover], since such elements generate
$I+J$. It therefore suffices to prove that $U(s)$ is disjoint from
$\widetilde Y$ for every $s\in I$. On the chart $U(s)$ the strict transform
of $Y=V(I)$ is cut out by the saturation of $I\cdot A[(I+J)/s]$ with respect
to $s$, that is, by

$$
I_s\cap A[(I+J)/s]
$$

formed inside $A_s$
([lemma-nagata-strict-transform-chart-closed]). Because $s\in I$ the
element $1=s/s$ lies in that ideal, so the ideal is the unit ideal and the
overlap of $U(s)$ with $\widetilde Y$ is empty.

For the second assertion put $I_j=\Gamma(X,\mathcal I_{Y_j})$. The centre
is $\sum_jI_j$, so the charts $U(s)$ for $s\in\bigcup_jI_j$ cover
$\widetilde X$. Fix such an $s$, say $s\in I_1$. The computation just made,
with $I=I_1$ and $J=I_2+\cdots+I_n$, shows $U(s)\cap\widetilde Y_1 =\varnothing$. Hence every point of $\widetilde X$ misses at least one
$\widetilde Y_j$, and the intersection of all of them is empty.
