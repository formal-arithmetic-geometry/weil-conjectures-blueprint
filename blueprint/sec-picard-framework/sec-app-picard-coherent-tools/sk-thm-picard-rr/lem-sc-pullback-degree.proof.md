+++
kind  = "proof"
of    = "lem-sc-pullback-degree"
+++
Since $\pi$ is finite flat, $\pi_*\mathcal O_C$ is locally free
of rank $d$, and the fibre over $P'$ is
$\operatorname{Spec}((\pi_*\mathcal O_C)\otimes k(P'))$, a
$k$-algebra of dimension $d$ (all residue fields are $k$
because $k$ is algebraically closed), whose length is

$$
\sum_{\pi(P)=P'}v_P(t_{P'})\,[k(P):k]
=\sum_{\pi(P)=P'}v_P(t_{P'}),
$$

as $\mathcal O_{C,P}$ is a discrete valuation ring with residue
field $k(P)$ ([lem-sc-point-cartier]). Hence
$\deg\pi^*[P']=\sum_{\pi(P)=P'}v_P(t_{P'})=d$, and the general
case follows by linearity.
