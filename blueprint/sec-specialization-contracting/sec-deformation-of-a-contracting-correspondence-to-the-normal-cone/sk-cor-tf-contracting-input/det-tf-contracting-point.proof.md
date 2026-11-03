+++
kind = "proof"
of = "det-tf-contracting-point"
uses = ["det-tf-contracting-restricted-morphism", "lem-trf-local-term-point", "def-trf-graph-correspondence"]
+++
Since $c_1^{-1}(y)$ is the reduced point $z$, $C_Z=(c_1^{-1}(y))_{\mathrm{red}}=\{z\}$, and both
legs of $c_Z$ map this point to the point $y=Z_{\mathrm{red}}\cong\operatorname{Spec}k$. So
$c_Z$ is the identity correspondence of $\operatorname{Spec}k$, its fixed scheme is the point,
and $F_{c_Z}\times_{F_c}\beta=\beta$. The restriction of $K$ to $y$ is the stalk $K_{\bar y}$,
and $c_{Z,2}^*$ and $c_{Z,1}^!$ are the identity on $D(\operatorname{Spec}k,A)$, so $u_Z$ is an
endomorphism of $K_{\bar y}$. For the identity correspondence of a point, the trace class is the
categorical trace under $\operatorname{Hom}(A_\beta,\omega_\beta)\cong A$, which is the
local term at the reduced point component ([lem-trf-local-term-point]).

If $c_1=\operatorname{id}_X$, then $e=i$, $c_{Z,1}=\mathrm{id}$, and the base-change mate
$e^*c_1^!K\to c_{Z,1}^!i^*K$ in [det-tf-contracting-restricted-morphism] is the identity of
$i^*K$. Hence $u_Z=e^*u=i^*u$, which is the stalk map $u_{\bar y}$.
