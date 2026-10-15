+++
kind  = "proof"
of    = "det-prop-scalar-six-ctf"
uses = ["det-prop-scalar-six-pullback", "sk-lem-sf-flat-model", "det-lem-int-tensor-shriek", "sk-cor-coefficient-heart-ii", "sk-lem-coefficient-heart", "sk-lem-int-integral-heart", "sk-prop-integral-criterion", "sk-thm-sf-ctf-stability", "sk-prop-sfb-cartesian-coefficients"]
+++
By [det-prop-scalar-six-pullback] (3) a composite of listed maps can be handled one
step at a time, so we may assume $\Lambda\to\Lambda'$ is one of the elementary maps.

*(1) Generators.* For a finite ring $A$ this is [sk-lem-sf-flat-model]: the
generators are $a_!L$ with $L$ locally constant with finite projective local
models. For $\Lambda=\mathcal O_E$ one has $\Dctf=\Dbc$, and
[det-lem-int-tensor-shriek] (2) writes every object as an iterated extension of
$a_!M$ with $M$ locally $P_0\otimes_{\mathcal O_E}\mathcal O_{E,S}$, $P_0$ a bounded complex of
finite free $\mathcal O_E$-modules. For $\Lambda=E$ or $\Qlb$, again $\Dctf=\Dbc$, and
by [sk-cor-coefficient-heart-ii] every object is obtained by finitely many cones
from $a_!L[n]$ with $L$ lisse, i.e. locally free of finite rank
([sk-lem-coefficient-heart]).

*(2) Local models.* If $P|_W\simeq P_0\otimes_{\Lambda(*)}\Lambda_W$ on a cover
$\{W\to S\}$, then, as $P_0$ is a complex of projective modules,
$$
P_{\Lambda'}|_W\simeq\Lambda'_W\otimes_{\Lambda_W}(P_0\otimes_{\Lambda(*)}\Lambda_W)=(\Lambda'(*)\otimes_{\Lambda(*)}P_0)\otimes_{\Lambda'(*)}\Lambda'_W,
$$
and $\Lambda'(*)\otimes_{\Lambda(*)}P_0$ is a bounded complex of finite projective
$\Lambda'(*)$-modules. So $P_{\Lambda'}$ is locally perfect. A locally perfect
complex $Q$ over $\Lambda'$ on $S$ lies in $\Dctf(S,\Lambda')$:
- for $\Lambda'$ a finite ring or a field ($E$, $F$, $\Qlb$), its cohomology sheaves
  are locally $H^q(Q_0)\otimes_{\Lambda'(*)}\Lambda'_W$ with $H^q(Q_0)$ finitely
  presented (the coefficient sheaves are flat over $\Lambda'(*)$, which is
  Noetherian or a field), so they are constructible on the single stratum $S$; and
  $Q$ has Tor amplitude in the amplitude of $Q_0$, since tensoring with a complex
  of flat modules is computed termwise;
- for $\Lambda'=\mathcal O_F$, $Q$ is locally a bounded complex of finite free
  $\mathcal O_{F,W}$-modules, hence derived complete (derived completeness is local) with
  constructible reduction, so $Q\in\Dbc(S,\mathcal O_F)=\Dctf(S,\mathcal O_F)$ by
  [sk-prop-integral-criterion].
Finally $a_!$ preserves $\Dctf$ ([sk-thm-sf-ctf-stability], or directly
[det-lem-int-tensor-shriek] (1) for $\mathcal O_F$), so $a_!(P_{\Lambda'})\in\Dctf(X,\Lambda')$.

*(3)* By [det-prop-scalar-six-pullback] (2), $(a_!P)_{\Lambda'}\simeq a_!(P_{\Lambda'})$,
which lies in $\Dctf(X,\Lambda')$ by (2). Extension of scalars is a triangulated
functor (a left derived functor), and additive, so it commutes with shifts,
cones and direct summands. The subcategory $\Dctf(X,\Lambda')$ is thick: it is
triangulated (for $\mathcal O_F$ by [sk-lem-int-integral-heart], for fields by
[sk-cor-coefficient-heart-ii], for finite rings by comparison with the étale
site where constructible sheaves form a weak Serre subcategory), Tor amplitude
bounds pass to cones and summands, and a direct summand of a constructible
sheaf is the image of an idempotent, hence constructible. Thus the class of
$K$ with $K_{\Lambda'}\in\Dctf(X,\Lambda')$ contains the generators of (1) and is
closed under the operations of (1), so it is all of $\Dctf(X,\Lambda)$.
