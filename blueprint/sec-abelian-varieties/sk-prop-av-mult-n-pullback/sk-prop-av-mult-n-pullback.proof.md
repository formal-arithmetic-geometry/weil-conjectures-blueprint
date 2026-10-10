+++
kind  = "proof"
of    = "sk-prop-av-mult-n-pullback"
uses = ["sk-prop-av-cube"]
+++
For $n=0$ the map $[0]$ factors through $\Spec k$, and every
invertible module on $\Spec k$ is free of rank one, so
$[0]^*\cN\cong\cO_A=\cN^{\otimes0}$. In the same way $0^*\cL\cong\cO_A$
for every invertible $\cL$, where $0=[0]$. For $n=1$ there is nothing
to prove.

Pull the cube relation of [sk-prop-av-cube] back along
$x\mapsto(x,x,-x)$: here $m_{123}(x,x,-x)=x$, $m_1=m_2=\mathrm{id}$,
$m_3=[-1]$, $m_{12}=[2]$ and $m_{13}=m_{23}=0$, so
$\cL^{\otimes3}\otimes[-1]^*\cL\cong[2]^*\cL$; for symmetric $\cN$
this reads $[2]^*\cN\cong\cN^{\otimes4}$. Next, for $n\ge1$, pull back
along $x\mapsto(x,x,[n-1]x)$: here $m_{123}=[n+1]$,
$m_1=m_2=\mathrm{id}$, $m_3=[n-1]$, $m_{12}=[2]$ and
$m_{13}=m_{23}=[n]$, giving

$$
[n+1]^*\cN\otimes\cN^{\otimes2}\otimes[n-1]^*\cN
\cong[2]^*\cN\otimes[n]^*\cN^{\otimes2}.
$$

Assume $[m]^*\cN\cong\cN^{\otimes m^2}$ for all $m\le n$ (true for
$n=1$ by the cases $m=0,1$). Since $\cN$ is invertible we may cancel
$\cN^{\otimes2}\otimes[n-1]^*\cN$, and obtain
$[n+1]^*\cN\cong\cN^{\otimes(4+2n^2-2-(n-1)^2)}=\cN^{\otimes(n+1)^2}$.
This completes the induction.
