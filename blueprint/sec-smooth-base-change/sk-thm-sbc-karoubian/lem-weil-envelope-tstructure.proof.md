+++
kind  = "proof"
of    = "lem-weil-envelope-tstructure"
+++
The shift conditions of [def-weil-t-structure] and the orthogonality are
preserved by retracts: the shift is an equivalence, and a morphism from a
retract of an object of $\mathcal T^{\le0}$ to a retract of an object of
$\mathcal T^{\ge1}$ is a retract of an element of the zero group
$\Hom_{\mathcal T}(A,B[-1])$, hence zero. For the truncation axiom,
functoriality of the truncation triangle $A(K)\to K\to C(K)\to A(K)[1]$ in
$K\in\mathcal T$ (with $A(K)=\tau^{\le0}K$, $C(K)=\tau^{\ge1}K$) applied to
the idempotent endomorphism $e:K\to K$ produces an idempotent endomorphism
$(e_{\le0},e,e_{\ge1})$ of the triangle; its components are idempotent
because the square of the endomorphism is the endomorphism induced by
$e^2=e$. Its image triangle in $\mathcal T^\natural$ is a retract of the
image of the truncation triangle, hence distinguished by
[lem-weil-karoubi-envelope-triangulated]; since $\tau^{\le0}K\in\mathcal
T^{\le0}$ and $\tau^{\ge1}K\in\mathcal T^{\ge1}$, the image triangle has the
requisite retract-factors $(\tau^{\le0}K,e_{\le0})\in(\mathcal
T^\natural)^{\le0}$ and $(\tau^{\ge1}K,e_{\ge1})\in(\mathcal
T^\natural)^{\ge1}$, and the image over all $K$ and $e$ gives the truncation
triangle axiom. For the heart: an object $(K,e)$ of the heart has zero
$\tau^{\le-1}$-part in the extended t-structure, so its truncation triangle
exhibits $(K,e)\cong H^0((K,e))$ $=(\mathcal H^0K,\mathcal H^0(e))$, with
$\mathcal H^0K\in\mathcal H(\mathcal T)$; conversely, for $A\in\mathcal
H(\mathcal T)$ and an idempotent $e$ of $A$, the object $(A,e)$ of $\mathcal
T^\natural$ is a retract of the image $(A,\operatorname{id}_A)$ of $A$, hence
lies in the heart. The two constructions are inverse up to the canonical
functor of [def-weil-karoubi-envelope], so the heart is exactly $\Kar(\mathcal
H(\mathcal T))$.
