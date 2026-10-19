+++
kind  = "proof"
of    = "sk-thm-nagata-compactification"
uses = ["sk-lem-nagata-sketch-affine-cover", "sk-thm-nagata-sketch-two-open", "thm-nagata-noetherian", "prop-nagata-noetherian-inverse-system", "lemma-nagata-separated-eventually", "lemma-nagata-finite-type-fp-model-system", "lemma-nagata-final-basechanged-compactification", "prop-nagata-finite-type-closed-in-fp", "sk-lem-nagata-sketch-closure"]
+++
*Noetherian base.* If $S$ is Noetherian, apply
[sk-lem-nagata-sketch-affine-cover] to obtain a finite affine cover
$X=U_1\cup\cdots\cup U_m$ with dense total intersection, each $U_r\to S$
being compactifiable, and induct on the unions $U_1\cup\cdots\cup U_r$.
At each step the overlap of $U_1\cup\cdots\cup U_r$ with $U_{r+1}$ contains
the dense total intersection. [sk-thm-nagata-sketch-two-open] gives a
compactification of the next union. The last union is $X$
([thm-nagata-noetherian]).

*Finite presentation over a qcqs base.* For a general qcqs $S$, first
suppose $X\to S$ is separated and of finite presentation. Absolute
Noetherian approximation gives

$$
S=\varprojlim_i S_i
$$

with $S_i$ Noetherian and affine transition maps (Stacks 01ZA;
[prop-nagata-noetherian-inverse-system], [lemma-nagata-separated-eventually]). Finite-presentation descent gives
a model $X_i\to S_i$, and at a later stage it is separated (Stacks 01ZM,
01ZQ; [lemma-nagata-finite-type-fp-model-system]). Compactify that model by the
Noetherian result and base change its compactification to $S$. Open
immersions and proper morphisms are stable under base change. Taking the
schematic closure of $X$ then ensures density
([sk-lem-nagata-sketch-closure], [lemma-nagata-final-basechanged-compactification]).

*Finite type.* Finally let $X\to S$ be only separated of finite type. The
finite-presentation envelope theorem (Stacks 01ZJ;
[prop-nagata-finite-type-closed-in-fp]) provides a closed immersion
$X\hookrightarrow X_0$ with $X_0\to S$ separated of finite presentation.
Compactify $X_0$ by the case already proved, and take the schematic closure
of $X$ in that compactification. Restricted to the open $X_0$, this closure
is exactly the closed subscheme $X$. Thus $X$ is open and schematically
dense in the closure, which is proper over $S$.

Both approximation results rest on an elementary affine fact: a finitely
presented algebra, its morphisms, and finitely many gluing identities
involve finitely many coefficients and equations, and so are defined at a
finite stage. The envelope step is needed because in a finite-type algebra
$R[x_1,\ldots,x_n]/I$ the ideal $I$ need not be finitely generated.
