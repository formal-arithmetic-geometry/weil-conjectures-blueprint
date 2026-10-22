+++
kind  = "proof"
of    = "lem-pc-genus-agrees-sc"
+++
By [def-sc-genus], $g(C)=\dim_kH^0(C,\Omega^1_{C/k})$, while the genus of
[def-pc-genus] is $\dim_kH^1(C,\mathcal{O}_C)$. Serre duality
([thm-sc-serre-duality-curve]) with $\mathcal M=\mathcal O_C$, $q=1$, $p=0$
gives a $k$-linear isomorphism
$H^1(C,\mathcal O_C)^\vee\cong H^0(C,\mathcal O_C^\vee\otimes\Omega^1_{C/k})
\cong H^0(C,\Omega^1_{C/k})$, and both spaces are finite-dimensional, so the
two dimensions agree.
