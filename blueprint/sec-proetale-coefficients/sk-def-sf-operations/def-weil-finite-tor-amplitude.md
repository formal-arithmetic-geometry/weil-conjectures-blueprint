+++
id = "def-weil-finite-tor-amplitude"
kind = "definition"
title = "Finite Tor amplitude"
order = 1823
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "sk-def-sfb-bounded-constructible", "sk-def-sfb-derived-tensor-hom"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an
integer $n\in\mathbf Z_{\geq1}$, and a scheme $Y$ on which $\ell$ is
invertible. Put $A_{E,n}=\mathcal O_E/\pi_E^n$, let
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring with
coefficient sheaf $\Lambda_Y=p_Y^*\Lambda$, and use the derived cohomology
sheaves [def-weil-derived-cohomology-sheaves] and the derived tensor product
over $\Lambda_Y$ ([sk-def-sfb-derived-tensor-hom]; [def-weil-derived-tensor]
for finite $\Lambda$). For an object $K\in D^b_c(Y,\Lambda)$ of the bounded
constructible category [sk-def-sfb-bounded-constructible] (for
$\Lambda=A_{E,n}$, with the finite-torsion constructibility condition
[def-weil-finite-torsion-constructibility]), say that $K$ has *finite Tor
amplitude* if there are integers $a\leq b$ such that, for every sheaf $M$ of
$\Lambda_Y$-modules placed in degree zero,

$$
 \mathcal H^r(K\otimes^L_{\Lambda_Y} M)=0
 \qquad\text{for every }r\in\mathbf Z\setminus[a,b].
$$

Define $D^b_{ctf}(Y,\Lambda)$ as the full triangulated subcategory of such
objects. The definition is the same for every $\Lambda$.

For $A_{E,n}$, finite Tor amplitude is an additional condition and does not
follow from bounded constructibility. For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$
it is automatic: every $K\in D^b_c(Y,\Lambda)$ with cohomology in $[a,b]$ has
Tor amplitude in $[a-1,b]$, so

$$
 D^b_{ctf}(Y,\Lambda)=D^b_c(Y,\Lambda)
 \qquad(\Lambda=\mathcal O_E,E,\Qlb),
$$

a theorem, [det-def-localizing-closure-ctf-equals-bc]. For
$\Lambda=\mathcal O_E$ it follows that all reductions
$K\otimes^L_{\mathcal O_{E,Y}}(A_{E,j})_Y$ of $K\in D^b_c(Y,\mathcal O_E)$
lie in $D^b_{ctf}(Y,A_{E,j})$ with Tor amplitude in one interval independent
of $j$.
