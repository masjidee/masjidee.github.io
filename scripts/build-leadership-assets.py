"""Generate public leadership PDFs and editable PowerPoint from shared JSON.
Install leadership/requirements.txt. Set MASJIDEE_FONT_DIR for DejaVu fonts.
"""
import json, os
from pathlib import Path
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'src/data/leadership.json').read_text())
OUT=ROOT/'public/docs/leadership';OUT.mkdir(parents=True,exist_ok=True)
FONTS=Path(os.environ.get('MASJIDEE_FONT_DIR','/usr/share/fonts/truetype/dejavu'))
for name,file in [('Body','DejaVuSans.ttf'),('BodyBold','DejaVuSans-Bold.ttf'),('Title','DejaVuSerif.ttf')]:pdfmetrics.registerFont(TTFont(name,str(FONTS/file)))
GREEN='#123F36';GOLD='#B59B5D';CREAM='#FBFAF2';MUTED='#526C59';LINE='#DCE3D3'
C=colors.HexColor
styles={}
for name,font,size,leading in [('label','BodyBold',8,12),('title','Title',30,35),('subtitle','Body',12,18),('meta','Body',8,12),('h2','Title',17,22),('body','Body',9.5,15),('bullet','Body',9.5,15),('cell','Body',8,12),('cellhead','BodyBold',8,12),('callout','BodyBold',9.5,15)]:
 styles[name]=ParagraphStyle(name,fontName=font,fontSize=size,leading=leading,textColor=C(MUTED if name in ['label','meta','subtitle'] else GREEN),spaceAfter=10,allowWidows=0,allowOrphans=0)
styles['h2'].spaceBefore=18;styles['h2'].keepWithNext=True
styles['bullet'].leftIndent=12;styles['bullet'].firstLineIndent=-10
P=lambda text,style='body':Paragraph(escape(text),styles[style])
def chrome(c,doc):
 w,h=A4;c.saveState();c.setFillColor(C(GREEN));c.setFont('BodyBold',9);c.drawString(45,h-31,'MASJIDEE');c.setFillColor(C(MUTED));c.setFont('Body',7);c.drawRightString(w-45,h-31,'LEADERSHIP SERIES · DISCUSSION DRAFT');c.setStrokeColor(C(LINE));c.line(45,h-40,w-45,h-40);c.line(45,39,w-45,39);c.setFont('Body',6.8);c.drawString(45,26,'Proof of concept / pilot · '+DATA['date']);c.drawRightString(w-45,26,str(doc.page));c.restoreState()
def panel(text,width,fill,style='callout'):
 table=Table([[P(text,style)]],colWidths=[width]);table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),C(fill)),('BOX',(0,0),(-1,-1),.5,C(LINE)),('LEFTPADDING',(0,0),(-1,-1),15),('RIGHTPADDING',(0,0),(-1,-1),15),('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),8)]));return table

def paper_pdf(paper):
 file=OUT/f"masjidee-{paper['slug']}.pdf";doc=SimpleDocTemplate(str(file),pagesize=A4,leftMargin=45,rightMargin=45,topMargin=61,bottomMargin=54,title=paper['title'],author='Masjidee project',subject='Leadership discussion draft; proof of concept and pilot')
 width=A4[0]-90;story=[P(paper['label'].upper(),'label'),P(paper['title'],'title'),P(paper['subtitle'],'subtitle'),P(paper['audience']+' · '+DATA['date'],'meta'),panel(paper['summary'],width,'#EAF0E2','body'),Spacer(1,10)]
 for section in paper['sections']:
  story.append(P(section['heading'],'h2'));story.extend(P(t) for t in section['paragraphs']);story.extend(P('• '+t,'bullet') for t in section['bullets'])
  if 'table' in section:
   data=[[P(x,'cellhead') for x in section['table']['headers']]]+[[P(x,'cell') for x in row] for row in section['table']['rows']]
   table=Table(data,colWidths=[width/len(data[0])]*len(data[0]),repeatRows=1,hAlign='LEFT');table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),C('#EAF0E2')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.4,C(LINE)),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story.extend([table,Spacer(1,10)])
  if 'callout' in section:story.extend([Spacer(1,5),panel(section['callout'],width,'#F0EDDF')])
 story.extend([Spacer(1,18),P('Prepared for evaluation and discussion. This document does not imply official Jamaat endorsement or production readiness.','meta')]);doc.build(story,onFirstPage=chrome,onLaterPages=chrome);print(file.relative_to(ROOT))

# Shared geometry in inches keeps the PDF deck and editable PowerPoint consistent.
def slide_ops(s,index):
 dark=s.get('kind') in ['cover','closing'];bg=GREEN if dark else CREAM;ink=CREAM if dark else GREEN;ops=[]
 def text(value,x,y,w,h,size=22,color=ink,font='Arial',bold=False):ops.append(dict(kind='text',value=value,x=x,y=y,w=w,h=h,size=size,color=color,font=font,bold=bold))
 def shape(kind,x,y,w,h,fill,line=None):ops.append(dict(kind=kind,x=x,y=y,w=w,h=h,fill=fill,line=line))
 text('MASJIDEE',.65,.32,3,.3,12,bold=True);text(s['kicker'],7.1,.35,5.55,.3,9,'#BACFA6' if dark else MUTED)
 shape('rect',.65,7.01,12,.012,'#4F705B' if dark else LINE);text('PROOF OF CONCEPT / PILOT · DISCUSSION DRAFT',.65,7.15,10,.2,8,'#C0D1AC' if dark else MUTED);text(f'{index+1:02d} / {len(DATA["slides"])}',11.9,7.13,.75,.25,9)
 if dark:
  text(s['title'],.75,1.45,9.1,2.45,58,font='Georgia')
  for j,point in enumerate(s['points']):text(point,.82,4.55+j*.58,9.3,.52,20,'#CFDFC0')
  shape('round',10.45,1.65,1.9,4.75,bg,'#6D8963');shape('oval',10.82,2.8,1.1,1.1,GOLD);shape('oval',11.07,2.68,1.08,1.08,bg)
 else:
  text(s['title'],.7,1,12,1.65,43,font='Georgia')
  if s.get('kind')=='three':
   for j,point in enumerate(s['points']):
    x=.7+j*4.06;shape('round',x,3.03,3.8,2.55,'#EAF0E2',LINE);text(f'0{j+1}',x+.23,3.3,1,.35,12,MUTED);text(point,x+.23,3.95,3.32,1.4,21)
  else:
   y=3;flow=s.get('flow')
   if s.get('kind')=='hierarchy':flow=['Global Jamaat / AMI','National · USA','Chapter · Oshkosh','Group → individuals']
   if flow:
    for j,item in enumerate(flow):
     x=.7+j*3.06;shape('round',x,2.95,2.76,.7,'#E7EEDC',LINE);text(item,x+.15,3.15,2.46,.4,16)
    y=3.95
   for j,point in enumerate(s['points']):text('•',.74,y+j*.67,.3,.6,22,GOLD);text(point,1.1,y+j*.67,11.4,.65,21)
 return bg,ops

def presentation():
 prs=Presentation();prs.slide_width=Inches(13.333333);prs.slide_height=Inches(7.5);prs.core_properties.title='Masjidee leadership briefing';prs.core_properties.author='Masjidee project';prs.core_properties.subject='Jamaat leadership discussion; proof of concept and pilot'
 pdf=canvas.Canvas(str(OUT/'masjidee-leadership-presentation.pdf'),pagesize=(960,540));pdf.setTitle('Masjidee leadership briefing');pdf.setAuthor('Masjidee project')
 for index,s in enumerate(DATA['slides']):
  slide=prs.slides.add_slide(prs.slide_layouts[6]);bg,ops=slide_ops(s,index);slide.background.fill.solid();slide.background.fill.fore_color.rgb=RGBColor.from_string(bg[1:]);pdf.setFillColor(C(bg));pdf.rect(0,0,960,540,stroke=0,fill=1)
  for op in ops:
   x,y,w,h=[op[k] for k in ['x','y','w','h']]
   if op['kind']=='text':
    shape=slide.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));frame=shape.text_frame;frame.word_wrap=True;frame.margin_left=frame.margin_right=frame.margin_top=frame.margin_bottom=0
    for i,line in enumerate(op['value'].split('\n')):
     p=frame.paragraphs[0] if i==0 else frame.add_paragraph();p.text=line;p.font.name=op['font'];p.font.size=Pt(op['size']);p.font.bold=op['bold'];p.font.color.rgb=RGBColor.from_string(op['color'][1:]);p.space_after=Pt(4)
    font='Title' if op['font']=='Georgia' else 'BodyBold' if op['bold'] else 'Body'
    style=ParagraphStyle('slide',fontName=font,fontSize=op['size'],leading=op['size']*1.2,textColor=C(op['color']));p=Paragraph(escape(op['value']).replace('\n','<br/>'),style);_,height=p.wrap(w*72,500)
    if height>h*72+12:raise ValueError(f'Slide {index+1} text exceeds its box: '+op['value'])
    p.drawOn(pdf,x*72,540-y*72-height)
   else:
    kind={'rect':MSO_SHAPE.RECTANGLE,'round':MSO_SHAPE.ROUNDED_RECTANGLE,'oval':MSO_SHAPE.OVAL}[op['kind']];shape=slide.shapes.add_shape(kind,Inches(x),Inches(y),Inches(w),Inches(h));shape.fill.solid();shape.fill.fore_color.rgb=RGBColor.from_string(op['fill'][1:])
    if op['line']:shape.line.color.rgb=RGBColor.from_string(op['line'][1:]);shape.line.width=Pt(.7)
    else:shape.line.fill.background()
    pdf.setFillColor(C(op['fill']));pdf.setStrokeColor(C(op['line'] or op['fill']));pdf.setLineWidth(.7)
    if op['kind']=='oval':pdf.ellipse(x*72,540-(y+h)*72,(x+w)*72,540-y*72,fill=1,stroke=bool(op['line']))
    elif op['kind']=='round':pdf.roundRect(x*72,540-(y+h)*72,w*72,h*72,8,fill=1,stroke=bool(op['line']))
    else:pdf.rect(x*72,540-(y+h)*72,w*72,h*72,fill=1,stroke=bool(op['line']))
  slide.notes_slide.notes_text_frame.text=s['notes'];pdf.showPage()
 pdf.save();prs.save(OUT/'masjidee-leadership-presentation.pptx');print('Presentation:',len(prs.slides),'slides, editable PowerPoint with speaker notes and PDF')
for paper in DATA['papers']:paper_pdf(paper)
presentation()

# CI verifies committed downloads against their shared editorial source.
import hashlib
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
manifest={'sourceSha256':sha(ROOT/'src/data/leadership.json'),'generatorSha256':sha(Path(__file__)), 'slides':len(DATA['slides']), 'files':{p.name:{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.suffix in ['.pdf','.pptx']}}
(OUT/'assets-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
