<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:from="rebelrunner_unformatted.xsd" 
    xmlns="rebelrunner.xsd" 
    >
    <xsl:include href="footer_links_inc.xsl"/>
    <xsl:include href="footer_logo_inc.xsl"/>

    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>

    <xsl:template match="from:Footer">
        <xsl:apply-templates select="." mode="footer_links"/> 
        <xsl:apply-templates select="." mode="footer_logo"/> 
    </xsl:template>


    <xsl:template match="*">
        <xsl:element name="{name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:copy/>
    </xsl:template>

    <xsl:template match="from:posts">
        <posts>
            <xsl:apply-templates select="@*|*"/>
        </posts>
    </xsl:template>

    <xsl:template match="from:posts/@source_url">
        <xsl:attribute name="source">popular</xsl:attribute>
    </xsl:template>
</xsl:stylesheet>
