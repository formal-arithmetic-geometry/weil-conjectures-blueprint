+++
kind  = "proof"
of    = "lemma-nagata-strict-transform-chart-cocycle"
uses = ["lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-power-torsion-kernel-localization"]
+++
Let $\Omega\subseteq Y\times_XX'$ be the open part lying over
$X\setminus V(\mathcal I)$ and put $C=C_a(A,B,I)$. On the chart
$\operatorname{Spec}(C)$ the preimage of $V(\mathcal I)$ is cut out by
$IC=aC$ ([lemma-nagata-chart-extended-ideal-principal]), so
$\Omega\cap\operatorname{Spec}(C)=D(a)$. By
[lemma-nagata-power-torsion-kernel-localization],
$\Gamma_{(a)}(C)$ is the kernel of $C\to C_a$, i.e. the ideal of the
scheme-theoretic closure of the quasi-compact open $D(a)$ in
$\operatorname{Spec}(C)$. Scheme-theoretic closures of quasi-compact
opens commute with restriction to opens, so the restriction of
$\Gamma_{(a)}(C)$ to $W$ is the ideal of the scheme-theoretic closure of
$\Omega\cap W$ in $W$. The same holds for the chart $c'$, and the two
restricted ideals coincide.
